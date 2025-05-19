
import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = "https://realpython.github.io/fake-jobs/"

# Send HTTP request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all job titles
job_elements = soup.find_all('h2', class_='title')

# Display job titles
print("Job Titles Scraped:")
for job in job_elements:
    print("-", job.text.strip())
