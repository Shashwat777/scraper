import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL='https://www.amazon.in/Apple-Watch-GPS-44mm-Space-Aluminium/dp/B07JB8DWGT/ref=sr_1_1?keywords=i+watch+apple&qid=1562683638&s=gateway&sr=8-1'
headers={"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
def chkprice():
 page=requests.get(URL,headers=headers)
 soup=BeautifulSoup(page.content,'lxml')
 title=soup.find(id="productTitle").get_text()
 price=soup.find(id="priceblock_ourprice").get_text()
 p=""
 for i in price :
    if(i!=","):
        p=p+i
 price=p
 cpr=float(price[2:8])
 if(cpr<40900.0):
    send_mail()



def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('shashwatjain.developer@gmail.com','shashwat@09')
    # subject='Price lowest'
    # body='check the link:https://www.amazon.in/Apple-Watch-GPS-44mm-Space-Aluminium/dp/B07JB8DWGT/ref=sr_1_1?keywords=i+watch+apple&qid=1562683638&s=gateway&sr=8-1'
    msg = """\
Subject: Lowest PRICE

check the link:https://www.amazon.in/Apple-Watch-GPS-44mm-Space-Aluminium/dp/B07JB8DWGT/ref=sr_1_1?keywords=i+watch+apple&qid=1562683638&s=gateway&sr=8-1"""
    server.sendmail(
        'shashwatjain.developer@gmail.com','shashwatjain2014@gmail.com',msg
    )
    print ("message sent")
    server.quit()
while(True):
    chkprice()
    time.sleep(60*60*24)


