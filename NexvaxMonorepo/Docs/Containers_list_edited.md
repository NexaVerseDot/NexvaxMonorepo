      **Containers list** 

**Common** 

• **opencex** \- main backend API 

• **opencexcel** \- Celery planner \+ bot’s tasks 

• **opencexwss** \- Websockets 

• **rabbitmq** \- RabbitMQ. Task queue for Celery 

• **redis** \- Redis. Cache, messaging with Celery and Websockets. 

• **postgresql** \- PostgreSQL DB 

• **nuxt** \- Server-side rendering (SSR) web server, used for static pages like 

homepage 

• **frontend** \- nginx \+ SPA frontend 

• **caddy** \- traffic router 

**Orderbooks & matching engine** 

• **opencex-matching** \- matching engine. By default, it starts without additional 

parameters and uses one container for all pairs. However, it is possible to run 

separate containers for each trading pair. 

◦ *python bin/stack.py \--pairs=BTC-ETH* \- only for BTC-ETH 

◦ *python bin/stack.py \--pairs=BTC-ETH, BTC-USDT* \- only for BTC-ETH, BTC 

USDT 

**BTC** 

• **opencex-btc** \- BTC processor. Block parsing, deposits, collection. 

• **bitcoind** \- BTC node 

**ETH** 

• **opencex-eth-blocks** \- block parsing 

• **opencex-eth-payouts** \- withdrawals processing 

• **opencex-eth-accumulations** \- collection of ETH 

• **opencex-erc-accumulations** \- collection of ERC20 

• **opencex-eth-deposits** \- ETH deposits 

• **opencex-eth-balances** \- pulls stuck fees and checks balances 

• **opencex-eth-gas** \- sending gas to addresses for collection 

**BNB** 

• **opencex-bnbblocks** \- block parsing 

• **opencex-bnbpayouts** \- withdrawals processing 

• **opencex-bnbaccumulations** \- collection of BNB 

• **opencex-bepaccumulations** \- collection of BEP20 

• **opencex-bnbdeposits** \- BNB deposits 

• **opencex-bnbbalances** \- pulls stuck fees and checks balances 

• **opencex-bnbgas** \- sending gas to addresses for collection 

**TRX** 

• **opencex-trxblocks** \- block parsing 

• **opencex-trxpayouts** \- withdrawals processing 

• **opencex-trxaccumulations** \- collection of TRX 

• **opencex-trcaccumulations** \- collection of TRC20 

• **opencex-trxdeposits** \- TRX deposits 

• **opencex-trxbalances** \- pulls stuck fees and checks balances 