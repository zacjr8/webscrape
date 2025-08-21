import requests
from bs4 import BeautifulSoup

# Example: search results page for "laptop" on Amazon
URL = "https://www.amazon.com/s?k=laptop"

# Adding headers to mimic a real browser (important for Amazon)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Send request
response = requests.get(URL, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.content, "html.parser")

# Find all product containers
results = soup.find_all("div", {"data-component-type": "s-search-result"})

# Loop through and extract title + price
for item in results[:10]:  # limit to first 10 results
    title = item.h2.text.strip() if item.h2 else "No title"
    
    price_whole = item.find("span", class_="a-price-whole")
    price_fraction = item.find("span", class_="a-price-fraction")
    if price_whole and price_fraction:
        price = price_whole.text + price_fraction.text
    else:
        price = "Not available"
    
    print(f"Product: {title}")
    print(f"Price: {price}")
    print("-" * 40)
