from exchange.settings import env

SCI_WITHDRAWAL_CHECK_TIMEOUT = 10*24*60*60 # ten days

SCI_TOPUP_FEE = {
    'advcash': 0.01,  # 1%
    'stripe': 0.01,  # 1%
}

# Stripe Configuration
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = env('STRIPE_WEBHOOK_SECRET')
STRIPE_API_VERSION = env('STRIPE_API_VERSION', default='2023-10-16')
STRIPE_ENABLED = env('STRIPE_ENABLED', default=False, cast=bool)
