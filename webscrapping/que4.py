import requests
from bs4 import BeautifulSoup

def scrape_naukri_job_listings(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all the job listing containers on the page
            job_listings = soup.find_all('article', class_='jobTuple')

            # Loop through each job listing container to extract details
            job_data = []
            for job in job_listings:
                # Extract job details like title, company, and location
                job_title = job.find('a', class_='title').text.strip()
                company_name = job.find('a', class_='subTitle').text.strip()
                job_location = job.find('li', class_='location').text.strip()

                # Append the extracted details to the list
                job_data.append({'title': job_title, 'company': company_name, 'location': job_location})

            return job_data
        else:
            print(f"Failed to fetch the URL: {url}, Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
url = 'https://www.naukri.com/fresher-jobs?src=discovery_trendingWdgt_homepage_srch'
job_data = scrape_naukri_job_listings(url)
if job_data:
    for job in job_data:
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print()
else:
    print("Failed to fetch job listings.")
