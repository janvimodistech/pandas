import requests
from bs4 import BeautifulSoup

def scrape_hindustan_times_news(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('div', class_='media')
            news_data = []
            for article in articles:
                headline = article.find('a', class_='media-heading').text.strip()
                summary = article.find('div', class_='media-txt').text.strip()
                url = article.find('a', class_='media-img')['href']
                news_data.append({'headline': headline, 'summary': summary, 'url': url})
            return news_data
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

url = 'https://www.hindustantimes.com/'
news_data = scrape_hindustan_times_news(url)
if news_data:
    for article in news_data:
        print(f"Headline: {article['headline']}")
        print(f"Summary: {article['summary']}")
        print(f"URL: {article['url']}")
        print()
else:
    print("Failed to fetch news data.")
