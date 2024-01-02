import requests
from bs4 import BeautifulSoup

def scrape_flipkart_product_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser') 
        product_name = soup.find('span', class_='B_NuCI').get_text(strip=True)
        product_price = soup.find('div', class_='_30jeq3').get_text(strip=True)      
        discount = soup.find('div', class_='_3Ay6Sb').get_text(strip=True)
        return {
            'Product Name': product_name,
            'Product Price': product_price,
            'Discount': discount
        }
    else:
        print(f"Failed to fetch the URL: {url}, Status Code: {response.status_code}")
        return None

url = 'https://www.flipkart.com/zest-4-toyz-globe-kids-stem-steam-educational-world-75mm-magnifying-glass-kids-office-globe-political-globe-globes-students-desk-table-top-political/p/itma7ca9ba52c5f5?pid=GLBFX3HEECBMFWBX&lid=LSTGLBFX3HEECBMFWBXBEZ6UM&marketplace=FLIPKART&store=dgv&srno=b_1_6&otracker=browse&fm=organic&iid=fc873112-6e59-4d76-9e3d-1424c54c9e31.GLBFX3HEECBMFWBX.SEARCH&ppt=browse&ppn=browse&ssid=z2zi2oftc00000001704211545295'
product_details = scrape_flipkart_product_details(url)
if product_details:
    for key, value in product_details.items():
        print(f"{key}: {value}")
else:
    print("Failed to fetch product details.")
