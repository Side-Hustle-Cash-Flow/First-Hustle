import requests
import urllib.request
import time
from bs4 import BeautifulSoup


url = 'http://leg.wa.gov/house/representatives/Pages/default.aspx'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

soup.select(".memberName")