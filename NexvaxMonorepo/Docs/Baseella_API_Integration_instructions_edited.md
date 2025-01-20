Baseella API Integration instructions 

**API Endpoint 3**   
**Authorization 3**   
**Requests 3** 

How to get a key for TOTP signatures 3  
**Directories 4**   
Countries 4   
Currencies 4   
**Creating transactions 5**   
Creation of the transaction itself 5   
Incoming 5   
Check method 5   
Creation method 5   
Parameters (min asset) 5   
Example of request body 7   
Sign method 7   
Outgoing 8   
Check method 8   
Creation method 8   
Parameters (min asset) 8   
Example of request body 10   
Sign method 10   
Internal 11   
Check method 11   
Creation method 11   
Parameters (min asset) 11   
Example of request body 11   
Sign method 12   
Exchange 14   
Calc method 14   
Parameters 14   
Example of request 14   
Response 14   
Example of response 15   
Creation method 15   
Parameters (min asset) 15   
Example of request body 16   
Sign method 16   
Nostro 17   
Check method 17   
Creation method 17   
Parameters (min asset) 17  
Example of request body 18   
Sign method 18   
**Signing of entities 20**   
Formation of the signature entity 20   
Forming a challenge 20   
Signing the challenge with TOTP code 20   
Signing the transaction 20   
Webhooks 21   
Webhook types 21   
Transactions (Outgoing, Incomin, Internal, Exchange, Nostro) change status 21   
Events 21   
Webhook content example 21   
Test request 21   
General ledger transactions change status 22   
Events 22   
Webhook content example 22   
Test request 22   
Customers (Corporate, Individual, COF) 23   
Events 23   
Webhook content example 23   
Applications (Corporate, Individual, COF) 23   
Events 23   
Webhook content example 23  
API Endpoint 

https://open-api-gateway.staging.baseella.com/ 

Authorization 

Access token is used for authorization. You need to put in request headers in follow way (example based on CURL) 

\-H 'Authorization: Bearer access\_token' \\ 

Requests 

All inquiries in the system are made on behalf of a system employee. Therefore it is necessary to integrate 

1\. Create a separate employee 

2\. Save his TOTP key for realization of transaction signing functionality in future. 3\. Save employee ID 

4\. Pass the employee ID to the headers of all requests in the following way (example based on CURL) 

\-H 'x-baseella-employee-id: 875ea718-5007-4c5f-afb2-cb2f185ac3d2' \\ 

How to get a key for TOTP signatures 

For an already created employee, you need to 

1\. Request password recovery 

2\. Set a new password using the link provided 

3\. Go to the authorization stage, enter login and password 

4\. At the next step you will be offered the key you are interested in. We recommend to copy the key, which is displayed under the QR code by clicking on it, or you can recognize it for the QR code  
Directories 

To work with the system there is a minimum necessary set of directories, which will be described further. 

Countries 

https://open-api-gateway.staging.baseella.com/\#/dictionaries/DictionariesController-listCount ries 

Countries are used in various methods, such as creating a transaction. The methods use the country ID, which you can get from the list of countries. 

Currencies 

https://open-api-gateway.staging.baseella.com/\#/dictionaries/DictionariesController-listCurre ncies 

A list of currencies is needed to get currency IDs for creating, receiving transactions and other operations.  
Creating transactions 

Creating a transaction is a multi-step operation consisting of the following steps 

1\. Creation of the transaction itself (incoming, outgoing, exchange, etc.). 2\. Formation of the signature entity 

3\. Signing the transaction 

Creation of the transaction itself 

Incoming 

Check method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsIncomingControll er-checkIncomingTransaction 

Before creating a transaction, we recommend calling the Check method, which checks if the transaction can be created with the parameters you need. 

The list of parameters is specified in the documentation. Parameter assignments are specified in the Transaction Creation section. 

The response will return 

● status \- Green or Red \- creation possible or not 

● Commissions \- if transactions will be applied to the transaction, full details on them will be kept. 

Creation method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsIncomingControll er-createIncomingTransaction 

Parameters (min asset) 

● **paymentType** \- 

○ List of all payment types 

■ FASTER\_PAYMENT 

■ BACS 

■ SEPA\_SCT\_INST 

■ SEPA\_SCT 

■ TARGET\_2 

■ SWIFT 

● **sum** 

○ Transaction amount  
○ Mandatory parameter 

● **currencyId** 

○ ID of currency of transaction 

○ Mandatory parameter 

● **recipientAccountNumber** 

○ the recipient's Baseella account number. The account number can be obtained from the customer data. 

○ Mandatory parameter 

● **pspPartnerId** 

○ ID of Bank partner for which funds have been received 

○ Mandatory parameter 

● **pspPartnerAccountNumber** 

○ ID of Bank partner account for which funds have been received ○ Mandatory parameter 

● **transferDate** 

○ Transaction creation date 

○ Mandatory parameter 

● **acceptedIn** 

○ Date of crediting funds to the account of the partner bank 

○ Mandatory parameter 

● **info** 

○ Purpose of payment or other related information 

○ Mandatory parameter 

**● senderAccountNumber** 

**○** Sender's account number (text field) 

○ Mandatory parameter 

**● remitterFullName** 

**○** Sender's name (text field) 

○ Mandatory parameter 

**● remitterAddress** 

**○** Sender's address (text field) 

○ Optional parameter 

**● remitterCity** 

**○** Sender's city (text field) 

○ Optional parameter 

**● remitterCountry** 

**○** Sender's address (text field) 

○ Optional parameter 

**● remitterBankSortCode** 

○ Sort code of sender Bank for Faster payment and BACS (text field with sort code structure validation) 

○ Required for Faster payment and BACS 

**● remitterBankBIC** 

○ SWIFT/BIC of sender Bank for SEPA SCT INST, SEPA SCT. TARGET 2, SWIFT (text field with SWIFT/BIC structure validation) 

○ Required for SEPA SCT INST, SEPA SCT. TARGET 2, SWIFT **● remitterBankName** 

**○** Sender's Bank name (text field)  
○ Optional parameter 

**● remitterBankAddress** 

**○** Sender's Bank address (text field) 

○ Optional parameter 

Example of request body 

{"paymentType":"FASTER\_PAYMENT","sum":88.35,"senderAccountNumber":"IB123456789 0000","recipientAccountNumber":"3.0.00.000001","currencyId":"58e5c99b-bd43-4ead-b0dd b8a9b52a2b08","pspPartnerAccountNumber":"2.1.00.000001","pspPartnerId":"a26ae78b-35 a7-4de5-a6a9-f1a59699029d","transferDate":"2024-07-21T06:46:04.000Z","acceptedIn":"20 24-07-21T06:46:04.000Z","info":"test","remitterFullName":"Dmitry 

Petrov","remitterBankSortCode":"10-00-00","remitterAddress":"Avenue 1","remitterCity":"London","remitterCountry":"1e57b0fe-af0d-457a-8eca-6b97069d463e","re mitterBankName":"Bank of 

England","remitterBankCountry":"1e57b0fe-af0d-457a-8eca-6b97069d463e","remitterBankA ddress":"Avenue 2"} 

Sign method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsIncomingControll er-createSignature 

The signing process is described in detail in the relevant section.  
Outgoing 

Check method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsOutgoingControll er-checkOutgoingTransaction 

Before creating a transaction, we recommend calling the Check method, which checks if the transaction can be created with the parameters you need. 

The list of parameters is specified in the documentation. Parameter assignments are specified in the Transaction Creation section. 

The response will return 

● status \- Green or Red \- creation possible or not 

● Commissions \- if transactions will be applied to the transaction, full details on them will be kept. 

Creation method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsOutgoingControll er-createOutgoingTransaction 

Parameters (min asset) 

● **paymentType** \- 

○ List of all payment types 

■ FASTER\_PAYMENT 

■ BACS 

■ SEPA\_SCT\_INST 

■ SEPA\_SCT 

■ TARGET\_2 

■ SWIFT 

● **sum** 

○ Transaction amount 

○ Mandatory parameter 

● **currencyId** 

○ ID of currency of transaction 

○ Mandatory parameter 

**● chargeType** 

○ List of possible values 

■ SHA 

■ BEN 

■ OUR 

○ Mandatory parameter 

**● senderAccountNumber** 

○ the sender Baseella account number. The account number can be obtained from the customer data.  
○ Mandatory parameter 

● **pspPartnerId** 

○ ID of Bank partner for which funds have been received 

○ Mandatory parameter 

● **pspPartnerAccountNumber** 

○ ID of Bank partner account for which funds have been received ○ Mandatory parameter 

● **transferDate** 

○ Transaction creation date (set up automatically at transaction sign action) ○ Optional parameter 

**● recipientAccountNumber** 

○ Recipient account number (text field) 

○ Mandatory parameter 

**● benificiaryFullName** 

○ Recipient full name (text field) 

○ Mandatory parameter 

**● benificiaryType** 

○ List of all payment types 

■ INDIVIDUAL 

■ CORPORATE 

○ Mandatory parameter 

**● benificiaryAddress** 

○ Recipient address (text field) 

○ Optional parameter 

**● benificiaryCity** 

○ Recipient address (text field) 

○ Optional parameter 

**● benificiaryCountry** 

○ Recipient country ID 

○ Optional parameter 

**● benificiaryBankBIC** 

○ SWIFT/BIC of recipient Bank for SEPA SCT INST, SEPA SCT. TARGET 2, SWIFT (text field with SWIFT/BIC structure validation) 

○ Required for SEPA SCT INST, SEPA SCT. TARGET 2, SWIFT 

**● benificiaryBankSortCode** 

○ Sort code of recipient Bank for Faster payment and BACS (text field with sort code structure validation) 

○ Required for Faster payment and BACS 

**● benificiaryBankName** 

○ Recipient bank name (text field) 

○ Optional parameter 

**● benificiaryBankCountry** 

○ Recipient bank Country ID 

○ Optional parameter 

**● benificiaryBankAddress** 

○ Recipient bank address (text field) 

○ Optional parameter 

● **info**  
○ Purpose of payment or other related information 

○ Mandatory parameter 

Example of request body 

{"chargeType":"SHA","recipientAccountNumber":"IB12345678900000","benificiaryFullName": "Dmitry 

Danilov","benificiaryBankCountry":"1e57b0fe-af0d-457a-8eca-6b97069d463e","benificiaryBa nkAddress":"Avenue 2","benificiaryBankSortCode":"10-00-00","benificiaryAddress":"Avenue 1","benificiaryBankName":"Bank of 

England","benificiaryType":"INDIVIDUAL","benificiaryCountry":"1e57b0fe-af0d-457a-8eca-6b 97069d463e","pspPartnerAccountNumber":"2.1.00.000001","paymentType":"FASTER\_PAY MENT","info":"test","currencyId":"58e5c99b-bd43-4ead-b0dd-b8a9b52a2b08","sum":1000,"s enderAccountNumber":"3.0.00.000002","pspPartnerId":"a26ae78b-35a7-4de5-a6a9-f1a5969 9029d","benificiaryCity":"London"} 

Sign method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsOutgoingControll er-createSignature 

The signing process is described in detail in the relevant section.  
Internal 

Check method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsInternalController checkInternalTransaction 

Before creating a transaction, we recommend calling the Check method, which checks if the transaction can be created with the parameters you need. 

The list of parameters is specified in the documentation. Parameter assignments are specified in the Transaction Creation section. 

The response will return 

● status \- Green or Red \- creation possible or not 

● Commissions \- if transactions will be applied to the transaction, full details on them will be kept. 

Creation method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsInternalController createInternalTransaction 

Parameters (min asset) 

**● sum** 

**○** Amount in fixed currency 

○ Mandatory parameter 

**● senderAccountNumber** 

○ the sender Baseella account number. The account number can be obtained from the customer data. 

○ Mandatory parameter 

**● recipientAccountNumber** 

○ the recipient Baseella account number. The account number can be obtained from the customer data. 

○ Mandatory parameter 

● **currencyId** 

○ ID of currency of transaction 

○ Mandatory parameter 

● **transferDate** 

○ Transaction creation date (set up automatically at transaction sign action) ○ Optional parameter 

Example of request body 

{"sum":88.35,"senderAccountNumber":"3.0.00.000002","recipientAccountNumber":"3.0.00.00 0001","currencyId":"58e5c99b-bd43-4ead-b0dd-b8a9b52a2b08", 

"transferDate":"2024-07-21T06:46:04.000Z","info":"test"}  
Sign method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsInternalController createSignature 

The signing process is described in detail in the relevant section.  
Exchange 

Calc method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsExchangeControll er-calcExchangeTransaction 

Parameters 

● **exchangeRateSourceId** 

○ exchange rate source ID 

○ Mandatory parameter 

● **exchangeDateOfRate** 

○ date and time for which the course will be taken from the selected source ○ Mandatory parameter 

**● exchangeCurrencyFromId** 

**○** ID of currency to be sold 

○ Mandatory parameter 

**● exchangeCurrencyToId** 

**○** ID of currency to be buy 

○ Mandatory parameter 

**● exchangeCurrencyFixedId** 

**○** Fixed currency (one of two From or To) 

○ Mandatory parameter 

**● sum** 

**○** Amount in fixed currency 

○ Mandatory parameter 

**● senderAccountNumber** 

○ the sender Baseella account number. The account number can be obtained from the customer data. 

○ Mandatory parameter 

**● recipientAccountNumber** 

○ the recipient Baseella account number. The account number can be obtained from the customer data. 

○ Mandatory parameter 

Example of request 

{"exchangeDateOfRate":"2024-07-22T11:07:12.268Z","exchangeRateSourceId":"20fd85b8-7 efa-4ce3-990d-85b629997f7b","exchangeCurrencyFromId":"58e5c99b-bd43-4ead-b0dd-b8a 9b52a2b08","exchangeCurrencyToId":"e22d39e4-e38a-4d42-8848-ab5e0518159b","exchan geCurrencyFixedId":"58e5c99b-bd43-4ead-b0dd-b8a9b52a2b08","sum":5555,"senderAccou ntNumber":"3.0.00.000002","recipientAccountNumber":"3.0.00.000002"} 

Response 

**● fixedAmount \-** Amount in fixed currency 

**● calculatedAmount \-** Opposit calculate amount  
**● baseRate \-** rate from reports rate source (configure att Administration/Settings/PSP details) 

**● rate \-** rate from selected rate source 

**● actualRate \-** rate from selected rate source \+ margin 

**● profitRate \-** result from “rate” 

**● marginPercent \-** margin percent from pre setup data 

**● profit \-** profit amount at calculate amount currency 

*Example of response* 

{ 

"data": { 

"fixedAmount": 5555, 

"calculatedAmount": 6524.81, 

"rate": 1.18644699, 

"baseRate": 1.18680276, 

"actualRate": 1.1745825201, 

"profitRate": 0.0118644699, 

"marginPercent": 1, 

"profit": 67.88 

} 

} 

Creation method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsExchangeControll er-createExchangeTransaction 

Parameters (min asset) 

● **exchangeRateSourceId** 

○ exchange rate source ID 

○ Mandatory parameter 

● **exchangeDateOfRate** 

○ date and time for which the course will be taken from the selected source ○ Mandatory parameter 

**● exchangeCurrencyFromId** 

**○** ID of currency to be sold 

○ Mandatory parameter 

**● exchangeCurrencyToId** 

**○** ID of currency to be buy 

○ Mandatory parameter 

**● exchangeCurrencyFixedId**  
**○** Fixed currency (one of two From or To) 

○ Mandatory parameter 

**● sum** 

**○** Amount in fixed currency 

○ Mandatory parameter 

**● senderAccountNumber** 

○ the sender Baseella account number. The account number can be obtained from the customer data. 

○ Mandatory parameter 

**● recipientAccountNumber** 

○ the recipient Baseella account number. The account number can be obtained from the customer data. 

○ Mandatory parameter 

**● transferDate** 

○ Transaction creation date (set up automatically at transaction sign action) ○ Optional parameter 

Example of request body 

{"sum":5555,"senderAccountNumber":"3.0.00.000002","recipientAccountNumber":"3.0.00.00 0002","exchangeDateOfRate":"2024-07-22T11:39:05.268Z","exchangeRateSourceId":"20fd8 5b8-7efa-4ce3-990d-85b629997f7b","exchangeCurrencyFromId":"58e5c99b-bd43-4ead-b0d d-b8a9b52a2b08","exchangeCurrencyToId":"e22d39e4-e38a-4d42-8848-ab5e0518159b","ex changeCurrencyFixedId":"58e5c99b-bd43-4ead-b0dd-b8a9b52a2b08","exchangeMarginPer 

cent":1,"exchangeActualRate":1.1745825201,"transferDate":"2024-07-22T11:39:05.000Z"} Sign method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsExchangeControll er-createSignature 

The signing process is described in detail in the relevant section.  
Nostro 

Check method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsNostroController checkNostroTransaction 

Before creating a transaction, we recommend calling the Check method, which checks if the transaction can be created with the parameters you need. 

The list of parameters is specified in the documentation. Parameter assignments are specified in the Transaction Creation section. 

The response will return 

● status \- Green or Red \- creation possible or not 

● Commissions \- if transactions will be applied to the transaction, full details on them will be kept. 

Creation method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsNostroController createNostroTransaction 

Parameters (min asset) 

**● sum** 

**○** Amount in fixed currency 

○ Mandatory parameter 

● **paymentType** \- 

○ List of all payment types 

■ FASTER\_PAYMENT 

■ BACS 

■ SEPA\_SCT\_INST 

■ SEPA\_SCT 

■ TARGET\_2 

■ SWIFT 

○ Mandatory parameter 

● **info** 

○ Purpose of payment or other related information 

○ Mandatory parameter 

**● senderAccountNumber** 

○ the sender Baseella Bank partner account number. The account number can be obtained from the customer data. 

○ Mandatory parameter 

**● recipientAccountNumber** 

○ the recipient Baseella Bank partner account number. The account number can be obtained from the customer data. 

○ Mandatory parameter 

● **currencyId**  
○ ID of currency of transaction 

○ Mandatory parameter 

● **transferDate** 

○ Transaction creation date (set up automatically at transaction sign action) ○ Optional parameter 

● **acceptedIn** 

○ Date of crediting funds to the account of the partner bank 

○ Mandatory parameter 

● **acceptedOut** 

○ Date of crediting funds to the account of the partner bank 

○ Mandatory parameter 

Example of request body 

{"currencyId":"58e5c99b-bd43-4ead-b0dd-b8a9b52a2b08","sum":1000,"paymentType":"SWI FT","transferDate":"2024-07-23T07:00:00.000Z","info":"test","senderAccountNumber":"2.1.0 0.000001","recipientAccountNumber":"2.1.00.000007"} 

Sign method 

https://open-api-gateway.staging.baseella.com/\#/transactions/TransactionsNostroController createSignature 

The signing process is described in detail in the relevant section.  
Signing of entities 

Formation of the signature entity 

Signature formation consists of several steps 

1\. Forming a challenge 

2\. Signing the challenge with TOTP code 

Forming a challenge 

https://open-api-gateway.staging.baseella.com/\#/signatures/SignaturesController-createTotp Challenge 

The result is a mfa token that will need to be signed with the employee's TOTP code. 

Signing the challenge with TOTP code 

https://open-api-gateway.staging.baseella.com/\#/signatures/SignaturesController-verifyTotp The result gives you a signature ID to use to sign the transaction you created. 

Signing the transaction 

Each transaction type describes a method for signing a transaction. 

It is necessary to pass to it 

1\. –transaction ID to the request 

2\. signature ID to the request body 

After the transaction is signed it will start its execution.  
Webhooks 

To customize webhook and sent events you need to specify Webhook URI in Adminstration/Settings/PSP details and enable Webhook Events that you are interested in. 

Webhook types 

Transactions (Outgoing, Incomin, Internal, Exchange, Nostro) change status 

Events 

● When the status of a transaction with the type incoming, outgoing, internal and exchange changes, the webhook with information is called: 

○ What was the status before the change 

○ To which status the transfer was made 

Any change sends an entity ID, to get data on it, you need to query it via API. 

Webhook content example 

const payload \= codec.decode(m.data) as { 

id: string; 

prevBaseellaStatus?: TransactionBaseellaStatus; 

currentBaseellaStatus?: TransactionBaseellaStatus; 

prevConsumerStatus?: TransactionConsumerStatus; 

currentConsumerStatus?: TransactionConsumerStatus; 

eventType?: WebhookEventType; 

}; 

Test request 

https://open-api-gateway.testing.baseella.com/\#/webhooks/WebhooksController-testOnTxSt atusChange  
General ledger transactions change status 

Events 

● When the status of a transaction with the type general ledger changes, the webhook with information is called: 

○ What was the status before the change 

○ To which status the transfer was made 

Any change sends an entity ID, to get data on it, you need to query it via API. 

Webhook content example 

const payload \= codec.decode(m.data) as { 

id: string; 

prev: GeneralLedgerTransactionStatus; 

current: GeneralLedgerTransactionStatus; 

eventType?: WebhookEventType; 

}; 

Test request 

https://open-api-gateway.testing.baseella.com/\#/webhooks/WebhooksController-testOnGLSt atusChange  
Customers (Corporate, Individual, COF) 

Events 

● Changing application data 

Any change sends an entity ID, to get data on it, you need to query it via API. 

Webhook content example 

const payload \= codec.decode(m.data) as { 

id: string; 

eventType?: WebhookEventType; 

}; 

Applications (Corporate, Individual, COF) 

Events 

● Creating an organization 

● Changing organization data 

Any change sends an entity ID, to get data on it, you need to query it via API. 

Webhook content example 

const payload \= codec.decode(m.data) as { 

id: string; 

eventType?: WebhookEventType; 

};