<template>
  <div class="modal-dialog modal-sm wallet-modal" role="document">
    <div class="modal-content">
      <div class="modal-body">
        <h3>{{ $t("common.depositAccountWith") }} {{ currency }}</h3>
        <hr />
        <form @submit.prevent="processStripePayment">
          <p class="title">
            {{ $t("common.amount") }}
            <span>
              ({{ $t("common.min") }}: <b>{{ depositLimits.min }}</b>
              {{ currency }} {{ $t("common.max") }}: <b>{{ depositLimits.max }}</b>
              {{ currency }})
            </span>
          </p>
          <input
            v-model="amount"
            v-numeric.number.decimal
            class="form-control input-modal"
            type="text"
            autocomplete="off"
          />
          <div id="stripe-elements"></div>
          <button 
            type="submit" 
            class="btn modal-action-button"
            :disabled="!isAmountValid || isProcessing"
          >
            {{ $t("common.proceed") }}
            <img
              width="20"
              class="float-right"
              src="/public/img/long-arrow-right.svg"
            />
          </button>
          <div class="error-modal">{{ errorMessage }}</div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { loadStripe } from '@stripe/stripe-js';
import getFixedDecimal from "~/mixins/getFixedDecimal";

export default {
  name: "WalletDepositStripeModal",
  mixins: [getFixedDecimal],
  props: {
    currency: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      amount: "",
      stripe: null,
      elements: null,
      card: null,
      errorMessage: "",
      isProcessing: false,
      serverDepositCalculatedWithFee: "0.00"
    };
  },
  computed: {
    depositLimits() {
      return this.coins[this.currency].limits.deposit[this.$config.currentTopUpCardPaySystem];
    },
    isAmountValid() {
      const amount = Number(this.amount);
      return amount >= this.depositLimits.min && 
             amount <= this.depositLimits.max &&
             this.serverDepositCalculatedWithFee !== "0.00";
    }
  },
  async mounted() {
    if (!this.localConfig.stripe?.publicKey) {
      console.error('Stripe public key not found');
      this.errorMessage = this.$t("common.configuration_error");
      return;
    }
    this.stripe = await loadStripe(this.localConfig.stripe.publicKey);
    this.elements = this.stripe.elements();
    this.card = this.elements.create('card');
    this.card.mount('#stripe-elements');
  },
  watch: {
    amount(newAmount) {
      if (newAmount && Number(newAmount) >= this.depositLimits.min) {
        this.calculateFeeOnServer({
          target_amount: Number(newAmount),
          currency: this.currency,
          gate_id: 10 // Stripe gateway ID
        });
      } else {
        this.clearServerDepositCalculatedFee();
      }
    }
  },
  methods: {
    clearServerDepositCalculatedFee() {
      this.serverDepositCalculatedWithFee = "0.00";
    },
    calculateFeeOnServer(data) {
      this.$http.post("sci/topup_amount/", data).then((response) => {
        this.serverDepositCalculatedWithFee = response.body.amount;
      });
    },
    async processStripePayment() {
      this.isProcessing = true;
      this.errorMessage = "";

      try {
        const { data: paymentIntent } = await this.$http.post("sci/stripe/create-payment/", {
          amount: this.serverDepositCalculatedWithFee,
          currency: this.currency.toLowerCase()
        });

        const result = await this.stripe.confirmCardPayment(paymentIntent.client_secret, {
          payment_method: { card: this.card }
        });

        if (result.error) {
          this.errorMessage = result.error.message;
        } else {
          await this.$http.post("sci/stripe/confirm-payment/", {
            payment_intent_id: result.paymentIntent.id
          });
          this.$modal.hide(WalletDepositStripeModal);
          this.$store.dispatch("core/getBalance");
        }
      } catch (error) {
        if (error.data?.non_field_errors) {
          this.errorMessage = error.data.non_field_errors[0];
        } else {
          this.errorMessage = this.$t("common.payment_failed");
        }
      } finally {
        this.isProcessing = false;
      }
    }
  },
  beforeDestroy() {
    if (this.card) {
      this.card.destroy();
    }
  }
};
</script>

<style scoped>
#stripe-elements {
  margin: 20px 0;
  padding: 10px;
  border: 1px solid var(--theme-border-color);
  border-radius: 4px;
}
</style>
