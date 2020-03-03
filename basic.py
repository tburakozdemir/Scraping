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



import datetime
from time import sleep
from getpass import getpass

def send_mail(username, password, receiver_mail, mail_subject, mail_body, server_incoming='smtp.gmail.com'):
    try:
        connection = smtplib.SMTP(server_incoming, 587)
        connection.ehlo()
        connection.starttls()
        connection.ehlo()

        connection.login(username, password)
        
        message = "Subject: {0}\n\n{1}".format(mail_subject, mail_body).encode("utf-8")

        connection.sendmail(username, receiver_mail, message)

        return 1
    except Exception as e:
        print(e, "\ncan not send mail")
        return 0
    finally:
        connection.close()



sender_mail = 'example@gmail.com'
password = getpass()
receiver_mail = 'example@gmail.com'

waiting_interval = 10

send_hour = 22
send_minute = 00 


# send_mail(sender_mail, password, receiver_mail, product_name, "")



is_sent_this_day = False # for sending only once
while(True):

    now = datetime.datetime.now()
    time_to_send = now.replace(hour=send_hour, minute=send_minute, second=0, microsecond=0)

    if(now > time_to_send and not is_sent_this_day):
    
        is_sent = send_mail(sender_mail, password, receiver_mail, product_name, "")
        # if mail is sent dont send again this day
        if(is_sent):
            is_sent_this_day = True

    elif(time_to_send > now):
        is_sent_this_day = False

    sleep(waiting_interval)



