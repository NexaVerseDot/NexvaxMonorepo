

**Settings** 

Backend (.env) 

Frontend 

Static pages 

**Backend (.env)** 

OpenCEX Backend settings are located here: 

/app/opencex/backend/.env 

In order for the settings to be applied, it is enough to restart the containers, for this you need to run the commands: 

cd /app/opencex/backend docker compose restart 

| Variable name  | Description  | Default |
| ----- | :---- | ----- |
| PROJECT\_NAME  | Give your project a name  | Opencex |
| ADMIN\_USER  | Email address of the Superuser created on deployment |  |
| FEE\_USER  | Email address of the user to which all the fees would be collected |  |
| ADMIN\_BASE\_URL  | URL suffix for admin panel |  |
| ADMIN\_MASTERPASS  | Second password for sensitive operations in the admin panel |  |
| DOMAIN  | The domain on which OpenCEX is deployed. |  |
| INSTANCE\_NAME  | Instance name :)   ('xxx\_prod', 'xxx\_dev', ...) | opencex |
| RECAPTCHA\_SECRET  | Google reCAPTCHA (server part, secret key) |  |
| CAPTCHA\_ALLOWED\_IP\_MASK  | IP mask when CAPTCHA is not used (for internal services, such as bots) | 172.\\d{1,3}.\\d{1,3}.\\d{1,3} |
| TELEGRAM\_CHAT\_ID  | Telegram chat ID used for other notifications. |  |
| TELEGRAM\_ALERTS\_CHAT\_ID  | Telegram chat ID used for  notifications: cryptocurrency  collection monitoring, worker  monitoring. |  |
| BTC\_SAFE\_ADDR  | Cold BTC address to which  cryptocurrency deposits will be collected. |  |
| ETH\_SAFE\_ADDR  | Cold ETH address to which  cryptocurrency deposits will be collected. |  |
| BNB\_SAFE\_ADDR  | Cold BNB address to which  cryptocurrency deposits will be collected. |  |

| TRX\_SAFE\_ADDR  | Cold TRX address to which  cryptocurrency deposits will be collected. |  |
| ----- | :---- | :---- |
| INFURA\_API\_KEY  | Credentials to Infura (used for requests on the ETH network) |  |
| INFURA\_API\_SECRET  | Credentials to Infura (used for requests on the ETH network) |  |
| ETHERSCAN\_KEY  | Credentials to Etherscan (used for requests on the ETH network) |  |
| BSCSCAN\_KEY  | Credentials to BSCscan (used for requests on the BNB network) |  |
| TRONGRID\_API\_KEY  | Credentials to Trongrid (used for requests on the TRX network) |  |
| EMAIL\_HOST  | Credentials to SMTP server, Host name. |  |
| EMAIL\_HOST\_USER  | Credentials to SMTP server. User name. |  |
| EMAIL\_HOST\_PASSWORD  | Credentials to SMTP server.  Password. |  |
| EMAIL\_PORT  | Credentials to SMTP server. Port 465 or 587 is mostly used |  |
| EMAIL\_USE\_TLS  | Credentials to SMTP server. Use TLS. | True |
| SUMSUB\_SECRET\_KEY  | KYC provider credentials  (SUMSUB) |  |
| SUMSUB\_APP\_TOKEN  | KYC provider credentials  (SUMSUB) |  |
| SUMSUM\_CALLBACK\_VALIDATI ON\_SECRET | KYC provider credentials  (SUMSUB) |  |
| SCORECHAIN\_BITCOIN\_TOKEN  | KYT provider credentials  (SCORECHAIN) |  |
| SCORECHAIN\_ETHEREUM\_TOK EN | KYT provider credentials  (SCORECHAIN) |  |

| TWILIO\_ACCOUNT\_SID  | SMS service credentials (TWILIO). Account SID. | none |
| :---- | :---- | :---- |
| TWILIO\_AUTH\_TOKEN  | SMS service credentials (TWILIO). Token. | none |
| TWILIO\_VERIFY\_SID  | SMS service credentials (TWILIO). SID. | none |
| TWILIO\_PHONE  | SMS service credentials (TWILIO). Phone number. | none |
| SENTRY\_DSN  | Project key in Sentry \- used for logs. | none |

**Frontend** 

OpenCEX Frontend settings are located here: 

/app/opencex/frontend/local\_config 

In order for the settings to be applied, you need to rebuild the image, for this you need to run the commands: 

cd /app/opencex/frontend/ git pull docker build \-t frontend \-f 

deploy/Dockerfile . cd /app/opencex/ docker compose up \-d \--force 

recreate 

| Variable name  | Description  | Default |
| :---- | ----- | :---- |
| recaptcha\_site\_key  | Google reCAPTCHA (client part, site key). |  |
| two\_fa  | Prefix for storing keys in Google Authenticator. | OpenCEX-2FA-\[email\] |
| project\_title  | Your exchange name, also used in the \<title\> tag. | OpenCEX |
| socials  | Links to social networks, channels |  |
| logo  | The path to your logo, if not  specified, the default is used. |  |

**Static pages** 

OpenCEX static pages (landing page) settings are located here: 

/app/opencex/nuxt/.env 

In order for the settings to be applied, you need to rebuild the image, for this you need to run the commands: 

cd /app/opencex/nuxt/ git pull docker build \-t nuxt \-f 

deploy/Dockerfile . cd /app/opencex docker compose up \-d \--force 

recreate 