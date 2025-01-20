1/19/25, 9:38 PM Celery tasks 

**Celery tasks** 

| Cancellation of overdue  withdrawals | every 15 minutes  | cancel\_expired\_withdrawals |
| :---- | :---- | :---- |
| Mark collected deposits  | every minute  | mark\_accumulated\_topups |
|  |  |  |
| Checking New ETH Blocks  | settings.ETH\_BLOCK\_GENERAT ION\_TIME | eth\_process\_new\_blocks |
| Checking ETH wallet balances  | settings.ETH\_ERC20\_ACCUMUL ATION\_PERIOD | eth\_check\_balances |
|  |  |  |
| ETH dust collection  | 0:00  | cryptocoins.tasks.eth.accumulate \_eth\_dust |
| Checking the performance of crypto workers | every hour X:00  | cryptocoins.tasks.commons.check \_crypto\_workers |
| User KYC update  | every 10 minutes  | plan\_kyc\_data\_update |
| Cleaning bot-bot matches  | 0:30  | bot\_matches\_cleanup |
| Clearing and merging order  editing transactions | 0:20  | auto\_transactions\_cleanup |
| Cleaning up Django sessions  | 0:10  | clear\_sessions |
| Clearing the AccessLog  | 0:11  | clear\_old\_logs |
| Clearing LoginHistory  | 0:12  | clear\_login\_history |
| Clearing OrderChangeHistory  | 0:13  | order\_changes\_cleanup |
| Clearing External Price History ExternalPricesHistory | 0:13  | external\_prices\_history\_cleanup |
| Clearing the minute chart  | 0:14  | trades\_aggregated\_cleanup |
| Clearing DifBalance  | 0:15  | clean\_old\_difbalances |
| Launching bots  | every 5 sec  | run\_bots |
| Updating the price of auto orders  | every minute  | otc\_orders\_price\_update |

| External Price Update with  Binance | every 15 sec  | update\_external\_exchanges\_pair s\_price\_cache |
| ----- | :---- | :---- |
| Updating external prices with Cryptocompare | every 30 sec  | update\_cryptocompare\_pairs\_pric e\_cache |
| Populating the UserPairDailyStat table | 5:01  | make\_user\_stats |
| Aggregation of all commissions to a special user | 4:01  | aggregate\_fee |
| Cache update with coin statisticsfor the last 24h | every minute | pairs\_24h\_stats\_cache\_update |
| Creating a minute chart | every minute | plan\_trades\_aggregation |
| Creating an Hourly Chart | every hour X:01 | plan\_trades\_aggregation |
| Creating a daily chart | 0:01 | plan\_trades\_aggregation |
| Calculation and caching of sat/b for Bitcoin | settings.SAT\_PER\_BYTES\_UPDATE\_PERIOD | cache\_bitcoin\_sat\_per\_byte |
| Daily statistics on cold wallets | 0:00 | calculate\_topups\_and\_withdrawals |
| Calculation of the deviation of balances (DifBalance) | 0:00 | calculate\_dif\_balances |
| Calculation of deviation of balances (DifBalance) for 10 days | every 10 days в 1:00 | calculate\_dif\_balances\_1m |
| Calculation of deposits/withdrawals by coins | 0:05 | fill\_inout\_coin\_stats |

