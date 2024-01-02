from bs4 import BeautifulSoup
import requests

def scrape_netflix_movie_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title_element = soup.find('h1', class_='title-title')
        year_element = soup.find('span', class_='title-info-metadata-item item-year')
        genre_element = soup.find('a', class_='title-info-metadata-item item-genre')
        synopsis_element = soup.find('div', class_='title-info-synopsis')
        title = title_element.text.strip() if title_element else 'Title not found'
        year = year_element.text.strip() if year_element else 'Year not found'
        genre = genre_element.text.strip() if genre_element else 'Genre not found'
        synopsis = synopsis_element.text.strip() if synopsis_element else 'Synopsis not found'
        return {
            'title': title,
            'year': year,
            'genre': genre,
            'synopsis': synopsis
        }
    else:
        print(f"Failed to fetch the URL: {url}, Status Code: {response.status_code}")
        return None

# Example usage
url = 'https://www.netflix.com/in/title/80017528?source=35'
movie_details = scrape_netflix_movie_details(url)
print(movie_details)
