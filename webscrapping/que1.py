import requests
from bs4 import BeautifulSoup
url = 'https://www.geeksforgeeks.org/courses?source=google&medium=cpc&device=c&keyword=gfg&matchtype=e&campaignid=20039445781&adgroup=147845288105&gad_source=1&gclid=Cj0KCQiAhc-sBhCEARIsAOVwHuTVAmdsHLpDuTEDSxwvPEJKIVo_OnzQ5cXDZNq7bLq-Arieevqqh24aAmKbEALw_wcB'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    for link in soup.find_all('a'):
        print(f"Link Text: {link.text}, URL: {link.get('href')}")
else:
    print(f"Failed to fetch the URL: {url}, Status Code: {response.status_code}")
