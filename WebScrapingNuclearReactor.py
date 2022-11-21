#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

f = open('powerreactor.csv', 'w', encoding = 'utf8', newline ='')
writer = csv.writer(f, delimiter = ',')
writer.writerow(['plantNameDocketNumber', 'licenseNumber', 'reactorType', 'location', 'ownerOperator', 'nRCRegion'])

url = 'https://www.nrc.gov/reactors/operating/list-power-reactor-units.html'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table')

for row in table.find_all('tr'):
    cells = row.find_all(['th', 'td'])
    plantNameDocketNumber = cells[0].text
    licenseNumber = cells[1].text
    reactorType = cells[2].text
    location = cells[3].text
    ownerOperator = cells[4].text
    nRCRegion = cells[5].text
    rowData = [plantNameDocketNumber, licenseNumber, reactorType, location, ownerOperator, nRCRegion]
    writer.writerow(rowData)


# In[6]:


df = pd.read_csv('powerreactor.csv')


# In[7]:


df.head(10)


# In[ ]:




