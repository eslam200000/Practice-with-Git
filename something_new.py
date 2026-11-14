import requests 
from bs4 import BeautifulSoup

url = "https://practice.scrapingcentral.com/challenges/static/tables/simple"

response = requests.get(url, timeout=10)
soup = BeautifulSoup(response.text, "lxml")

rows = soup.select("table#products-table tbody tr")
products = []
for row in rows:
    products.append({
        "sku": row.select_one("td:first-child").get_text(strip=True),
        "name": row.select_one("td:nth-child(2)").get_text(strip=True),
        "brand": row.select_one("td:nth-child(3)").get_text(strip=True),
        "price": row.select_one("td:nth-child(4)").get_text(strip=True),
        "stock": row.select_one("td:nth-child(5)").get_text(strip=True),
    })
