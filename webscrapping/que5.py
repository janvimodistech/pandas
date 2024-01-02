import requests
import json
from bs4 import BeautifulSoup

def scrape_gfg_data(url):
    try:
        response = requests.get(url)       
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')           
            data = {
                'title': soup.title.string,
                'meta_description': soup.find('meta', attrs={'name': 'description'}).get('content', ''),
                'h1_tags': [tag.text.strip() for tag in soup.find_all('h1')],
                
            }
            with open('gfg_data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print('Data has been scraped and saved to gfg_data.json')
        else:
            print(f"Failed to fetch the URL: {url}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
url = 'https://www.geeksforgeeks.org/'
scrape_gfg_data(url)
