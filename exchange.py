import smtplib
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import schedule
import time


def exchange():
        #General purpose event schedular
        my_url = 'https://finance.yahoo.com/quote/USDTRY=X/'
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html,"html.parser")
        
        #Div class where dolar and percentage
        containers = page_soup.findAll("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})
        
        #Variables
        USDTORTY = containers[0].find_all('span')[0].string
        USDTORTYPERCENTAGE = containers[0].find_all('span')[1].string
        
        print("TRY TO USD: "+ USDTORTY, "PERCANTAGE: " +  USDTORTYPERCENTAGE)
        mail()


schedule.every(1).minutes.do(exchange)
schedule.every().hour.do(exchange)
schedule.every().day.at("10:30").do(exchange)

while 1:
        schedule.run_pending()
        time.sleep(1)
