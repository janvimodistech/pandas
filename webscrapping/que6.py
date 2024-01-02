from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def scrape_weather_data(url):
    try:
        # Set up the Selenium WebDriver
        options = Options()
        options.headless = True  # Run Chrome in headless mode
        service = Service('C:/WebDriver/bin/chromedriver.exe')
 # Replace with the path to your chromedriver executable
        driver = webdriver.Chrome(service=service, options=options)

        # Load the page
        driver.get(url)

        # Wait for the temperature element to be visible
        temperature_element = driver.find_element(By.CLASS_NAME, 'CurrentConditions--primary--2SVPh')
        temperature = temperature_element.find_element(By.TAG_NAME, 'span').text.strip()

        # Print the scraped data
        print(f"Temperature: {temperature}")

        # Quit the WebDriver
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'https://weather.com/en-IN/india/news/news/2024-01-02-severe-cold-dense-fog-delhi-punjab-rajasthan-up-mp'
scrape_weather_data(url)
