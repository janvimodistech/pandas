from selenium import webdriver
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
driver = webdriver.Chrome(options=options)
url = 'https://finance.yahoo.com/quote/CL%3DF?p=CL%3DF'
driver.get(url)
driver.implicitly_wait(10)  
soup = BeautifulSoup(driver.page_source, 'html.parser')
price_element = soup.find('span', {'data-reactid': '50'})
stock_price = price_element.text if price_element else 'N/A'
volume_element = soup.find('td', {'data-test': 'TD_VOLUME-value'})
stock_volume = volume_element.text if volume_element else 'N/A'
print(f"Stock Price: {stock_price}")
print(f"Stock Volume: {stock_volume}")
driver.quit()
