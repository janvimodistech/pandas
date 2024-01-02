import requests
from bs4 import BeautifulSoup
base_url = 'https://github.com/search?q=python&type=repositories&p='
num_pages = 3
for page in range(1, num_pages + 1):
    url = f'{base_url}{page}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.find_all('div', class_='f4 text-normal')
        for item in items:
            print(item.text.strip())

    else:
        print(f"Failed to fetch the URL: {url}, Status Code: {response.status_code}")

   
    print(f"Fetched URL: {url}")
