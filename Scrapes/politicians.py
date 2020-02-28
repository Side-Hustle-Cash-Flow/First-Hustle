import requests
import urllib.request
import time
from bs4 import BeautifulSoup

'''
Politicians.py is replist.py with class structure for best practicies





url = 'http://leg.wa.gov/house/representatives/Pages/default.aspx'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
'''
#soup.select(".memberName")

#global 
members = []
members_dict = dict()


class ParsedOfficial:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def name(self): # packs members in array as an array First name, Last name, Party
        soup_members = self.soup.find_all('span',class_='memberName')
        for member in soup_members:
            m = member.text
            m = m.split()
            m.pop(0)
            members.append(m)

    def address(self):
        pass
    def district(self): 
        pass
    def commities(self):
        pass
    def email(self):
        pass
    def votes(self): #votes are stored in pdf and will need to be converted to csv. python package Tabula will be used for this
        '''
        how to get vote .pdf
        div id="allMembers"
        '''
        pass
        
        

