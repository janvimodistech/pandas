import requests
from bs4 import BeautifulSoup
import sqlite3
def create_database():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT,
                      year INTEGER,
                      genre TEXT,
                      synopsis TEXT)''')
    conn.commit()
    conn.close()
def scrape_netflix_movie_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        title_element = soup.find('h1', class_='title-title')
        year_element = soup.find('span', class_='title-info-metadata-item item-year')
        genre_element = soup.find('a', class_='title-info-metadata-item item-genre')
        synopsis_element = soup.find('div', class_='title-info-synopsis')

        if title_element and year_element and genre_element and synopsis_element:
            title = title_element.text.strip()
            year = int(year_element.text.strip())
            genre = genre_element.text.strip()
            synopsis = synopsis_element.text.strip()

            conn = sqlite3.connect('movies.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO movies (title, year, genre, synopsis) VALUES (?, ?, ?, ?)',
                           (title, year, genre, synopsis))
            conn.commit()
            conn.close()

            return {'title': title, 'year': year, 'genre': genre, 'synopsis': synopsis}
        else:
            print("Failed to find one or more elements.")
            return None
    else:
        print(f"Failed to fetch the URL: {url}, Status Code: {response.status_code}")
        return None


def main():
    create_database()
    url = 'https://www.netflix.com/in/title/80017528?source=35'
    movie_details = scrape_netflix_movie_details(url)
    if movie_details:
        print("Scraped and stored movie details successfully!")

if __name__ == "__main__":
    main()
