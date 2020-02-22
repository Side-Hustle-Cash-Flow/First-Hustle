import requests
import urllib.request
import time
from bs4 import BeautifulSoup


url = 'http://leg.wa.gov/house/senators/Pages/default.aspx'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

pols = soup.select(".memberName")

print(pols)