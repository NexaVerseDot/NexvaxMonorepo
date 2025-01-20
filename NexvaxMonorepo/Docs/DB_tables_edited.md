

**DB tables** 

Authentication 

Main tables 

Service tables 

User notifications via email and popup alerts 

Settings 

**Authentication** 

| account\_emailaddress  | confirmation of user email addresses |
| :---- | :---- |
| auth\_group  | permissions group names |
| auth\_group\_permissions |  |
| auth\_permission  | permissions |
| auth\_user  | users |
| auth\_user\_groups |  |
| auth\_user\_user\_permissions |  |
| authtoken\_token |  |
| core\_expiringtoken |  |

**Main tables** 

| bots\_botconfig  | configs for trading bots |
| :---- | :---- |
| bots\_ordermatch  | bot trade statistics in Order Creation mode |
| bots\_ordermatchstat  | bot trade statistics aggregated by day in the Order Creation mode |
| core\_accesslog  | history of requests to API and administrative interface |
| core\_balance  | user balances |
| core\_difbalance  | daily statistics on balance discrepancies |
| core\_difbalancemonth  | 10-day statistics on balance discrepancies |
| core\_disabledcoin  | disabled coins |
| core\_exchange  | all exchanges |
| core\_executionresult  | all matches |
| core\_externalpriceshistory  | external price history BTC, ETH to USD |
| core\_feesandlimits  | commissions and limits on coins |
| core\_order  | all exchange orders |
| core\_orderchangehistory  | order change history (volume, price) |
| core\_orderrevert  | order reverses |
| core\_orderstatechangehistory  | history of order state changes (fields state, status) |
| core\_pairsettings  | trading pair settings. Enable/Disable Auto Orders for Pairs |
| core\_profile  | user profiles |
| core\_sendfund  | p2p transactions |
| core\_sendfundsrevert  | reverse p2p transactions |
| core\_smshistory  | history of phone number changes and confirmations via SMS to withdraw funds from the exchange |
| core\_tradesaggregatedstats  | chart data |
| core\_transaction  | all exchange transactions |

| core\_transactionprice |  |
| :---- | :---- |
| core\_twofactorsecrethistory  | history of exclusions/disconnections of 2FA users |
| core\_twofactorsecrettokens  | 2FA tokens |
| core\_userexchangefee  | personal commissions for users |
| core\_userfee  | personal commissions for users |
| core\_userkyc  | KYC |
| core\_userlimitsstats  | user statistics on deposits and withdrawals, trades for the month and year |
| core\_userpairdailystat  | daily trading statistics of users |
| core\_userrestrictions  | disabling deposits / withdrawals, the ability to create orders for the user |
| core\_userwallet  | all wallets on the exchange |
| core\_wallethistoryitem  | wallet change history |
| core\_wallettransactions  | cryptocurrency deposits |
| core\_wallettransactionsrevert  | reverts of cryptocurrency deposits |
| core\_withdrawallimitlevel  | types of withdrawal limits |
| core\_withdrawaluserlimit  | user withdrawal limit |
| core\_withdrawalrequest  | all currency withdrawals from the exchange |
| cryptocoins\_accumulationdetails  | used to verify the collection address on a cold wallet |
| cryptocoins\_accumulationstate  | current state of collection from the user's wallet |
| cryptocoins\_accumulationtransaction  | collection transactions from user wallets |
| cryptocoins\_depositswithdrawalsstats  | daily statistics on cold wallets |
| cryptocoins\_gaskeeper  | gas keepers |
| cryptocoins\_keeper  | keepers |
| cryptocoins\_lastprocessedblock  | stores the id of the last parsed blocks of coins |

**Service tables** 

| django |  |
| :---- | :---- |
| django\_admin\_log |  |
| django\_content\_type |  |
| django\_migrations |  |
| django\_session |  |
| django\_site |  |
| otp\_totp\_totpdevice  | 2FA for administrative interface |

**User notifications via email and popup alerts** 

| notifications\_mailing |  |
| :---- | :---- |
| notifications\_mailing\_users |  |
| notifications\_mailingprocessed |  |
| notifications\_notification |  |
| notifications\_notification\_users |  |

**Settings** 

| settings\_field |  |
| :---- | :---- |
| settings\_instance |  |
| settings\_setting |  |
| settings\_value |  |

