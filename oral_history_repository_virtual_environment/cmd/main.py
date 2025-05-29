import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/search?q=bangladesh'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print("html body "+soup.body)


# the bbc has the paths, /news/articles/