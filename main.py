from bs4 import BeautifulSoup
import requests
from smtplib import *

AMAZON_URL ="https://www.amazon.in/Apple-iPhone-13-Mini-128GB/dp/B09G9FNN4X/ref=sr_1_3?crid=3GINNZQUAXPTO&keywords=iphone+13+mini&qid=1657861151&sprefix=iphone+13+m%2Caps%2C914&sr=8-3"
BUYING_PRICE = 60000

my_email = "email"
password = "password"

header={
    "Accept-Language": "en-US,en;q=0.9,gu;q=0.8,hi;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49"
}


amazon_response = requests.get(url=AMAZON_URL, headers=header)
amazon_html = amazon_response.text

soup = BeautifulSoup(amazon_html, "html.parser")

amazon_product = soup.find(name="span", class_="a-offscreen")
amazon_product_price = float(amazon_product.getText().replace("₹", "").replace(",", ""))
print(amazon_product_price)

if amazon_product_price < BUYING_PRICE:
    connection = SMTP("smtp-mail.outlook.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="user_email",
                        msg=f"Subject:Price drop Alert!\n\n Iphone 13 mini getting at {amazon_product_price},"
                            f"URL: {AMAZON_URL}")
    connection.close()

