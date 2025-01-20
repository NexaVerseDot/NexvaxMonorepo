

**Files and classes** 

**Contents** 

admin\_panel 

bin 

bots 

core 

cryptocoins 

exchange 

lib 

locale 

notifications 

public\_api 

sci 

seo 

**admin\_panel** 

Django admin panel backend 

**bin** 

**stack.py** \- used to run a matching engine for a pair. 

Examples: 

python stack.py – launches the order book for all the pairs. Such a command is used on a test environment and launches all order books in one container. 

python stack.py –pairs=BTC-USDT – launches the order book for the BTC-USDT pair. This command is used in production. Each pair has a separate container. 

**bots** 

All about bots 

• **exchanges/** \- classes with a single interface for working with exchanges via API (placement of orders, balances, etc.) 

• **bot.py** – the main logic of the bots and strategies. Launches the bot according to the settings (BotConfig). 

• **cache.py** – caches used in bots 

• **models.py** – models used by bots 

◦ BotConfig – bot settings 

◦ LiquidityStat 

◦ LiquidityMatch 

◦ OrderMatch 

◦ OrderMatchStat 

• **structs.py** \- Data structures used in bot logic 

• **tasks.py** – Celery tasks: 

◦ check\_bot – Runs botconfig 

◦ check\_bots – Checks all botconfigs to see if they are ready to run. Calls 

check\_bot task 

◦ calculate\_liquidity\_stats – performs daily calculation of liquidity statistics 

**core** 

The core of the system. Contains all the necessary minimum for the operation of the exchange 

• **api\_urls/** \- Internal API endpoints categorized 

• **auth/** \- components related to authentication and authorization. 

◦ adapters.py \- Contains a custom AccountAdapter 

◦ api\_hmac\_auth.py \- Class for working with HMAC authentication. Uses 

api\_key, secret\_key from user profile 

◦ backends.py \- Contains the CIUsernameAuthBackend class, which prevents a user brute force attack by measuring the response time 

◦ token\_auth.py \- Used for authorization in websockets 

• **consts/** \- Constants and global variables 

◦ currencies.py \- Global variables with lists of coins, tokens and their parameters ◦ dif\_balance.py \- Types of differential balances (used to monitor balance   
differences) 

◦ facade.py \- Constants with information on coins and tokens 

◦ gates.py \- Contains the GATES global variable required for fiat handlers to work ◦ inouts.py \- Constants used in deposits/withdrawals 

◦ orders.py \- Constants used in orders 

◦ pairs.py \- pair IDs 

• **exceptions/** \- exceptions categorized 

• **filters/** \- filters for GET requests 

• **lib/** 

◦ inouts.py \- contains a base class for creating external integrator handlers for fiat deposit/withdrawal 

• **models/** 

◦ cryptocoins  

▪ UserWallet \- user's wallet. Also used for storing keepers, if user\_id is empty 

◦ facade  

▪ Profile – user profile. Also contains API keys 

▪ UserFee \- personal commission for the user. Used when matching orders 

▪ UserExchangeFee \- personal commission for the user. Used for swap 

▪ TwoFactorSecretTokens \- 2FA for users 

▪ Message \- allows you to leave a message to the user 

▪ TwoFactorSecretHistory \- user's 2FA status change history 

▪ UserKYC – KYC 

▪ SourceOfFunds \- SOF. 

▪ ExpiringToken \- used for authentication 

▪ LoginHistory \- user login history. Saved IP and user-agent 

▪ AccessLog \- logs of requests to the back, incl. to the admin panel 

▪ SmsHistory \- History of changing the phone number and status of 

confirmation of withdrawals via SMS 

▪ UserRestrictions \- allows you to prohibit making deposits / withdrawals, 

orders for a specific user 

▪ CoinInfo \- general (reference) information on the coin 

◦ inouts/balance.py  

▪ Balance \- current wallet balances. 

◦ inouts/dif\_balance.py 

▪ DifBalance \- the difference between the balance in the Balance table and 

the calculated amount of deposits/withdrawals/trades is stored 

◦ inouts/disabled\_coin.py 

▪ DisabledCoin \- disabling any functionality of the coin (deposits, 

withdrawals, trades, exchanges, etc.) 

◦ inouts/fees\_and\_limits.py 

▪ FeesAndLimits \- limits and commissions for the selected currency. 

▪ WithdrawalFee \- withdrawal fee for coins and tokens 

◦ inouts/pairs\_settings.py 

▪ PairSettings \- various settings for couples 

◦ inouts/sci.py 

▪ PayGateTopup \- fiat deposits 

▪ PayGateTopupRevert \- rollbacks of fiat deposits 

◦ inouts/transaction.py 

▪ Transaction – exchange transaction. Should be created whenever the 

balance of the main wallet (Balance model) should change. 

◦ inouts/wallet.py 

▪ WalletTransactions \- cryptocurrency deposits 

▪ WalletTransactionsRevert \- rollbacks of cryptocurrency deposits 

◦ inouts/withdrawal.py 

▪ WithdrawalRequest \- crypto and fiat withdrawals. 

▪ WithdrawalLimitLevel \- reference book with monthly withdrawal limits 

▪ WithdrawalUserLimit \- Monthly withdrawal limit for a specific user 

◦ orders 

▪ Order \- an order to buy or sell crypto 

▪ OrderChangeHistory \- history of order changes 

▪ OrderStateChangeHistory \- history of order state changes 

▪ OrderRevert \- rollback of a completed order 

▪ Exchange \- completed exchanges crypto \<-\> fiat 

▪ ExecutionResult \- order matches 

◦ stats 

▪ UserPairDailyStat, TradesAggregatedStats \- data for charts 

▪ ExternalPricesHistory \- history of rates from external exchanges 

▪ InoutsStats \- daily statistics on deposits / withdrawals by coin 

◦ wallet\_history 

▪ WalletHistoryItem \- history of transactions with the user's wallet 

(deposits/withdrawals, freezes, etc.). Displayed in the personal account in 

the section with wallets 

• **orderbook** 

◦ actions.py \- Contains a class for updating the order book in the cache, creating order books grouped by the number of characters, notifying web sockets about 

the order book change 

◦ helpers.py \- functions for working with the order book 

◦ book.py \- work with orders, formation of order books 

◦ stack.py \- contains the glass class used by the order book 

• **serializers/** \- serializers with input parameter validation, categorized. 

◦ auth.py \- Serializers related to authentication. If it is necessary to change the login/registration/password change/password reset/captcha check logic, then 

first of all look in this file 

◦ cryptocoins.py 

◦ facade.py 

◦ inouts.py 

◦ orders.py 

◦ stats.py 

◦ wallet\_history.py 

◦ withdrawal.py 

• **signal\_handlers/** \- Django signals are stored here, usually generated when 

creating / changing a model object 

• **signals/** \- custom Django signals 

• **tasks/** 

◦ facade.py  

▪ pong \- periodically checks if websockets are alive 

▪ plan\_kyc\_data\_updates \- check for the latest KYC update. If necessary, it 

launches a task to update KYC data for the user 

▪ update\_kyc\_data\_for\_user \- updates KYC data for a user 

▪ clear\_sessions \- clear the django session 

▪ clear\_old\_logs \- delete old records in AccessLog 

▪ clear\_login\_history \- delete old login history entries (LoginHistory). Leaves 

100 latest records for each user 

▪ notify\_sof\_verification\_request\_admin \- send email to admin when creating 

SOF 

▪ notify\_sof\_verification\_request\_user \- send email to user when creating 

SOF 

▪ notify\_sof\_request\_status\_changed\_user \- send email to user when SOF 

status 

▪ changed notify\_user\_ip\_changed \- sending a letter to the user that there 

was an attempt to login from a new ip address 

▪ notify\_failed\_login \- send a letter to the user that there was an attempt to 

login with an incorrect password 

◦ inouts.py  

▪ cancel\_expired\_withdrawals \- cancels unconfirmed withdrawals after N 

minutes 

▪ sync\_currencies\_with\_db \- creates new entries in DisabledCoin when 

adding new coins after restarting the service 

▪ send\_sepa\_details\_email \- send SEPA details to a user 

▪ withdrawal\_failed\_email \- send an email to the user about the failure of the 

withdrawal 

▪ process\_withdrawal\_requests \- send fiat withdrawals 

▪ calculate\_dif\_balances \- calculation of difference in balances (DifBalance) 

▪ clean\_old\_difbalances \- clean up old DifBalance entries 

▪ send\_withdrawal\_confirmation\_email \- send an email to the user with a link 

to confirm the withdrawal 

◦ orders.py  

▪ place\_order \- placing an order through the orderbook processor 

▪ update\_order\_wrapped \- order editing through the orderbook processor 

▪ cancel\_order \- order cancellation via orderbook handler 

▪ market\_order \- creating a market order through the order book processor 

▪ exchange\_order \- creating an exchange through the orderbook processor 

▪ stop\_limit\_order \- creating a stop-limit order through the orderbook 

processor 

▪ stop\_limit\_processor \- stop limit order processor 

▪ otc\_orders\_price\_update \- schedules price updates for pairs with auto 

orders enabled 

▪ run\_otc\_orders\_price\_update \- updates the price of auto orders for the 

specified pair using prices from external exchanges 

▪ pairs\_24h\_stats\_cache\_update \- update 24h stats for coins 

▪ aggregate\_fee \- creates a transaction that charges a special user (fee user) 

a commission for all transactions over the past day to the balance 

▪ bot\_matches\_cleanup \- cleaning bot-bot matches and corresponding 

orders, transactions 

▪ send\_api\_callback \- callback when order state changes 

▪ send\_order\_changed\_api\_callback\_request \- callback when order state 

changes 

▪ send\_exchange\_completed\_message \- sends a message to the user about 

the completion of the exchange 

▪ send\_exchange\_expired\_message \- sends a message to the user that the 

deal is expired 

▪ cleanup\_old\_order\_changes \- removes old entries in OrderChangeHistory 

▪ cleanup\_extra\_transactions \- collapses order editing transactions 

◦ stats.py  

▪ make\_user\_stats \- creates entries in UserPairDailyStat 

▪ update\_external\_exchanges\_pairs\_price\_cache \- updates cache with 

external rates 

▪ update\_cryptocompare\_pairs\_price\_cache \- updates the cache with rates 

from cryptocompare.com 

▪ plan\_trades\_aggregation \- plans to run data for charts 

▪ do\_trades\_aggregation\_for\_pair \- creates data for charts for the selected 

pair and period 

▪ cleanup\_old\_prices\_history \- delete old external rates history records 

▪ trades\_aggregated\_cleanup \- deleting old records according to the 

schedule 

▪ vacuum\_database \- starting a database vacuum 

▪ fill\_inout\_coin\_stats \- filling stats for daily deposits/withdrawals by coin 

• **templates/** \- Email Templates 

• **templatetags/** \- custom template functions. 

• **utils/** 

◦ stats/ \- functions for working with charts, various statistics 

◦ auth.py \- JWT handler 

◦ cleanup\_utils.py \- functions for cleaning the database from unused data 

◦ facade.py \- contains the sitemap generation function, work with caching urls for the callback 

◦ inouts.py \- functions for working with deposits/withdrawals 

◦ limits.py \- limit validator for orders 

◦ wallet\_history.py \- contains functions for working with wallet history. 

• **views/** \- views divided into categories 

• **websockets/** \- contains routes for urls and web socket commands 

• **admin.py** \- admin resources 

• **apps.py** \- initialization of the core application. Also from here is the initialization of django custom signal handlers 

• **balance\_manager.py** \- Class for working with the main balance 

• **cache.py** \- caches and keys for caches used by the kernel 

• **currency.py** \- contains classes that define currencies, parameters of coins and tokens 

• **middleware.py** \- Middleware classes for django.  

◦ AccessLogsMiddleware \- writes django access logs to the core.AccessLog 

table 

◦ force\_default\_language\_middleware \- ignores Accept-Language HTTP headers ◦ SetupTranslationsLang \- allows you to change the response language using   
the API\_LANG header 

• **otcupdater.py** \- Work with updating the price of auto orders 

• **pairs.py** \- Classes for working with pairs. It also sets a list of pairs present on the exchange 

• **permissions.py** \- auxiliary classes for checking permissions used by views 

• **stack\_processor.py** \- Classes and functions for stack operation. Is the main class for the operation of glasses 

• **translations.py** \- registration of models and fields that can have multiple 

languages 

• **withdrawal\_processor.py** \- classes for working with fiat withdrawals 

**cryptocoins** 

Cryptocoins and tokens, cryptointegrators, alerts 

• **coins/** \- Contains modules that define coins. In **init.py** of each module, data on a coin / token is indicated and it is registered in global variables 

• **cold\_wallet\_stats/** \- contains stats handlers for cold wallets: current balance, balance for the previous day, deposits, withdrawals, delta 

• **interfaces/** \- auxiliary classes for integrating coins, which work in a similar way to ethereum (BNB, TRX) 

• **management/commands** \- custom Django console commands  

◦ btcworker.py \- launch BTC integrator  

◦ generate\_keeper.py \- create a keeper for the specified coin 

• **models/** 

◦ accumulation\_details.py  

▪ AccumulationDetails \- Stores the details of cryptocurrency collections. Used 

for monitoring 

◦ accumulation\_state.py  

▪ AccumulationState \- stores the current state of the wallet for ether coins 

◦ accumulation\_transaction.py  

▪ AccumulationTransaction \- used to separate gas transactions from deposits 

◦ keeper.py  

▪ Keeper \- coin keepers  

▪ GasKeeper \- gas keepers (used to send gas to a wallet that requires token 

collection) 

◦ last\_processed\_block.py  

▪ LastProcessedBlock \- stores the number of the last verified block of the 

specified blockchain 

◦ proxy.py \- proxy models for the admin panel 

◦ scoring.py  

▪ TransactionInputScore \- stores the calculated scoring of the transaction  

▪ ScoringSettings \- scoring settings 

◦ stats.py  

▪ DepositsWithdrawalsStats \- stats on deposits/withdrawals 

• **monitoring/** \- module for monitoring deposits and checking fees. For each coin, a separate processor is created, which pulls information about address transactions from third-party sources (Etherscan, Tronscan, etc.) and compares it with the 

internal exchange. 

• **scoring/** \- classes for scoring 

• **tasks/** 

◦ bnb.py/eth.py/trx.py \- tasks for the operation of the corresponding coins. Are 

full-fledged integrators 

◦ btc.py  

▪ cache\_bitcoin\_sat\_per\_byte \- calculates sat/b value using mempool. The 

calculated value is cached for the time 

settings.SAT\_PER\_BYTES\_UPDATE\_PERIOD 

◦ commons.py  

▪ check\_accumulations \- Check collection addresses and verify against an 

encrypted cold wallet. Sends an alert when there is a mismatch.  

▪ mark\_accumulated\_topups \- schedules the launch of monitoring deposits 

through external sources  

▪ mark\_accumulated\_topups\_for\_currency \- launches monitoring for the 

selected coin  

▪ check\_crypto\_workers \- checks the performance of cryptoworkers by 

comparing the current block of the network with the last checked one. 

◦ scoring.py  

▪ process\_defered\_deposit \- used in bitcoin-like integrators to give some time 

for transaction to be verified for KYT before collecting. 

◦ stats.py  

▪ calculate\_topups\_and\_withdrawals \- calculation of deposits/withdrawals per 

day 

• **utils/** \- auxiliary functions for cryptocurrencies 

• **accumulation\_manager.py** \- used in ETH-like workers to manage collection state • **admin.py** \- admin panel resources 

• **cache.py** \- caches involved in the operation of the "cryptocoins" application 

• **coin\_service.py** \- contains the base class of the bitcoin-like coin integrators 

**exchange** 

Django's base directory containing global settings, routes, and more 

• **settings/** \- project settings divided into categories. Each file contains default 

settings and is stored in the repository. In order to redefine a variable in any 

configuration file, you must create a file with the same name, prefixed with "local\_". For example, if you need to change the ENABLE\_OTP\_ADMIN setting from the  **admin.py** file, you need to create a **local\_admin.py** file and set the desired value for ENABLE\_OTP\_ADMIN in this file. 

◦ admin.py \- settings related to the admin panel 

◦ auth.py \- authentication, registration 

◦ bots.py \- bot settings 

◦ celery.py \- celery settings. Enable/disable groups of periodic tasks. 

◦ common.py \- Django settings and general settings. 

◦ cors.py \- configuration for CORS lib. 

◦ crypto.py \- various settings related to cryptocurrencies: cold addresses, keys for services and nodes, etc. 

◦ databases.py \- database connection settings. 

◦ email.py \- credentials for sending email. 

◦ exchange.py \- various exchange settings. 

◦ i18n\_l10n.py \- localization and internationalization settings for django. 

◦ kyc.py \- KYC and SumSub settings 

◦ logging.py \- configuring global loggers. 

◦ nodes.py \- settings for connecting to cryptocurrency nodes. 

◦ redis.py \- Redis settings. 

◦ rest.py \- Django Rest Framework settings. 

◦ sci.py \- service settings for working with fiat or partner platform. 

◦ scoring.py \- scoring settings, credentials for accessing scoring services. 

◦ sentry.py \- settings for error logging in sentry. 

◦ twilio.py \- credentials for Twilio. 

• **api\_urls.py** \- routes involved in the internal API 

• **asgi.py** \- entry point for ASGI applications 

• **celery.py** \- initialize celery 

• **celery\_app.py** \- celery configuration, queuing, task scheduling 

• **loggers.py** \- helper classes for logging 

• **models.py** \- base classes for project models 

• **notifications.py** \- websocket command handlers 

• **routing.py** \- global websocket routing 

• **urls.py** \- global project routing 

• **views.py** \- 404 error handler 

• **wsgi.py** \- entry point for WSGI applications 

**lib** 

	Various auxiliary modules and clients for third-party services

* **cryptointegrator/** \- contains functions and classes for bitcoin-like cryptointegrators.  
* **services/** \- clients for third-party services.  
* **backup\_utils.py** \- functions for creating backups when cleaning bot-bot matches  
* **batch.py**  
* **cache.py** \- Create prefixed caches  
* **cipher.py** \- AES encryption  
* **countless\_pagination.py** \- infinite paginator used in views  
* **exceptions.py** \- base class for client-side exceptions in the project  
* **fields.py** \- custom fields of models and serializers  
* **filterbackends.py** \- custom filters for GET requests in views  
* **helpers.py** \- various small helper functions  
* **json\_encoder.py** \- custom classes for rendering json views  
* **mixins.py** \- various mixins  
* **notifications.py** \- functions for sending notifications in various ways  
* **oneinstlock.py** \- helper classes for creating order book workers  
* **orders\_helper.py** \- helper functions for working with orders  
* **permissions.py** \- custom permissions for vbuh  
* **serializers.py** \- various serializers  
* **tasks.py** \- tools for synchronous execution of celery tasks  
* **throttling.py** \- classes for throttling  
* **utils.py** \- helper functions  
* **views.py** \- mixins for views

##         **locale** 	Internationalization files

## **notifications**

## Creation of mass notifications for users through the admin panel

## **public\_api**

## Public API module

## **sci**

## Fiat integrators

## **seo**

## Static coin pages, blog, homepage

* ## api\_urls.py \- Endpoints for internal API

* ## models.py

  * ## Tag \- assigned to one / several posts for searching by tags

  * ## Post \- post model

  * ## ContentPhoto \- allows you to upload pictures and get the url of the picture for its further use, for example, on third-party resources

  * ## CoinStaticPage \- used to create static pages for coins.

  * ## CoinStaticSubPage \- used to create static subpages related to a particular coin.

* ## translation.py \- models are specified for which it is necessary to have fields in several languages

* ## validators.py \- functions for validating blog inputs

## 

      

