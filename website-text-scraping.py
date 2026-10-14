import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")

response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("Title:", soup.title.get_text(strip=True) if
      soup.title else "No title")
print("\nText:")
print(soup.get_text("", strip=True))

#pip install requests beautifulsoup4


