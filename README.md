# Stock_News_Alerting_Project
This project is mainly for users who trade and purchase stock, but can also be used by anyone who is interested in a stock of a specific company. 
The main objective of this program is to alert a user via SMS when their stock has fluctuated by 5%. This is demoed using the stock of Tesla(TSLA). 

For this project, three APIs were used:
- Alphavantage, which is the API used to retrieve daily stock data, with the API endpoint: https://www.alphavantage.co/query
- NewsAPI, which is the API used to get the article(news) related to the company of that stock. API endpoint: https://newsapi.org/v2/everything
- Twilio, which is used to send SMSes, instead of using an API endpoint for Twilio - the Twilio package was installed, and from there Twilio was imported. 
