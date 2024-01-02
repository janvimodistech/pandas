import requests
from bs4 import BeautifulSoup

def scrape_recipe_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title_element = soup.find('h1', class_='headline')
        ingredients_elements = soup.find_all('span', class_='ingredients-item-name')
        instructions_elements = soup.find_all('span', class_='recipe-directions__list--item')

        title = title_element.text.strip() if title_element else 'Title not found'
        ingredients = [ingredient.text.strip() for ingredient in ingredients_elements]
        instructions = [instruction.text.strip() for instruction in instructions_elements]

        return {
            'title': title,
            'ingredients': ingredients,
            'instructions': instructions
        }
    else:
        print(f"Failed to fetch the URL: {url}, Status Code: {response.status_code}")
        return None

url = 'https://www.allrecipes.com/recipe/68488/creamy-cajun-chicken-pasta/'
recipe_details = scrape_recipe_details(url)
if recipe_details:
    print(recipe_details)
else:
    print("Failed to scrape recipe details.")
