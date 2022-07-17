import requests
from bs4 import BeautifulSoup
import smtplib, ssl
import lxml

my_email = "higherstudyadmission@gmail.com"
password = "wahwogxwxcpkjvlq"
product_title = ""
current_price = 0
link_of_product = ""

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,bn;q=0.8,ms;q=0.7"
}
url = "https://www.amazon.com/AmazonBasics-Mid-Back-Office-Chair-Armrests/dp/B00IIFW2L4/ref=sxin_13_trfob_0_B00IIFW2L4?content-id=amzn1.sym.d1687343-4d33-4fc8-8397-a05b9928ee2a%3Aamzn1.sym.d1687343-4d33-4fc8-8397-a05b9928ee2a&cv_ct_cx=gaming+chairs&keywords=gaming+chairs&pd_rd_i=B00IIFW2L4&pd_rd_r=83708121-e012-4d7e-8199-183460ff1468&pd_rd_w=ZYFu9&pd_rd_wg=eIcJH&pf_rd_p=d1687343-4d33-4fc8-8397-a05b9928ee2a&pf_rd_r=944B32F3227DVPSD2M5E&qid=1658091313&sr=1-1-eef91bd8-9d31-490c-8bb3-80f02876f902"

response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
price = soup.find(class_="a-offscreen").getText()
price_without_currency = float(price.split("$")[1])

if price_without_currency < 60:
    product_title = soup.find(id="productTitle").getText()
    current_price = soup.find(class_="a-offscreen").getText()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="sabbir.cse.duet@gmail.com",
                            msg=f"Subject: AmaZon Product\n\n {product_title}\n{current_price}\n{url}")
