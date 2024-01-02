import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.geeksforgeeks.org/courses?source=google&medium=cpc&device=c&keyword=gfg&matchtype=e&campaignid=20039445781&adgroup=147845288105&gad_source=1&gclid=Cj0KCQiAhc-sBhCEARIsAOVwHuTVAmdsHLpDuTEDSxwvPEJKIVo_OnzQ5cXDZNq7bLq-Arieevqqh24aAmKbEALw_wcB'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    data = []

    for link in soup.find_all('a'):
        link_text = link.text.strip()
        link_url = link.get('href').strip() if link.get('href') else ''
        data.append([link_text, link_url])

    with open('links.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Link Text', 'URL'])
        writer.writerows(data)

    print('Data has been saved to links.csv')
else:
    print(f"Failed to fetch the URL: {url}, Status Code: {response.status_code}")
