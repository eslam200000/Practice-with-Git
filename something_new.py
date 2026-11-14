import requests 

url = "https://practice.scrapingcentral.com/challenges/static/tables/simple"

response = requests.get(url, timeout=10)