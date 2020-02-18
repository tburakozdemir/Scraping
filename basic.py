import smtplib
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#Example website
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
#opening up connetion, grabbing the page
uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()
#html parsing
page_soup = soup(page_html,"html.parser")
# grabs each product
containers = page_soup.find_all("div" ,{"class":"item-container"})

for container in containers:
    brand_container = container.findAll("a", {"class":"item-brand"})

    brand_name = brand_container[0].img["title"]

    product_container = container.findAll("a", {"class":"item-title"})

    product_name = product_container[0].text
    
    
    #shipping_container = container.findall("li" , {"class":"price-ship"})
    #shipping = shipping_container[0].text.strip()

    #print("Brand: " + brand_name)
    #print("Product Name: " + product_name)
    #print("Shipping: " + shipping)


mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('example@gmail.com','Password')

mail.sendmail('example@gmail.com','example@gmail.com',product_name)

mail.close()





