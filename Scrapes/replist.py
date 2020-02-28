import requests
import urllib.request
import time
from bs4 import BeautifulSoup


url = 'http://leg.wa.gov/house/representatives/Pages/default.aspx'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

#soup.select(".memberName")

#global 
members = []
members_dict = dict()



def name():
    soup_members = soup.find_all('span',class_='memberName')
    for member in soup_members:
        m = member.text
        m = m.split()
        m.pop(0)
        members.append(m)

def names():
    locator = 'div.memberInformation div.memberColumnPad div.col-csm-8'
    name_item = soup.select_one(locator)
    print(name_item)
def district():
    pass
def commities():
    pass

def memberNames(): # packs members in array as an array First name, Last name, Party

        

    print(len(members))
    


names()
#memberNames()
#print(members)
'''

print(len(members))
m = members[1].split()

m_dict = {m[1] + ' ' + m[2]: m[3]}

print(m_dict)
'''
#find_reps()
#find_rep_links()