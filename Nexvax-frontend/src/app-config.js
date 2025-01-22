const PaySystems = {
  cauri: "cauri",
  payeer: "payeer",
  sepa: "sepa",
  stripe: "stripe"
};

export default {
  supportedLanguages: ["en", "ru"],
  defaultLanguage: "ru",
  currentWithdrawCardPaySystem: PaySystems.stripe,
  currentTopUpCardPaySystem: PaySystems.stripe,
  PaySystems,
};
