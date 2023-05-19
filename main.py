import requests
from bs4 import BeautifulSoup

# Send a GET request to the job website
url = "https://example.com/jobs"  # Replace with the URL of the job website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the job elements on the page
job_elements = soup.find_all("div", class_="job")

# Extract the details from each job element
for job_element in job_elements:
    # Extract job title
    title = job_element.find("h2").text.strip()
    
    # Extract company name
    company = job_element.find("span", class_="company").text.strip()
    
    # Extract location
    location = job_element.find("span", class_="location").text.strip()
    
    # Extract job description
    description = job_element.find("div", class_="description").text.strip()
    
    # Print the job details
    print("Title:", title)
    print("Company:", company)
    print("Location:", location)
    print("Description:", description)
    print("--------------------")
