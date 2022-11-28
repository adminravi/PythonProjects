from bs4 import BeautifulSoup
import requests


unfamiliar_skill = input('Enter the skill to filter out: :')
print(f'filtering out: {unfamiliar_skill}')

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

for job in jobs:
    recent_jobs = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in recent_jobs:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']
        if unfamiliar_skill is not skills:
          print(f'Company name: {company_name.split()}')
          print(f'Required Skills: {skills.split()}')
          print(f'More Info: {more_info}')
          print(f'Posting date: {recent_jobs}')
          print("------------------------------")
