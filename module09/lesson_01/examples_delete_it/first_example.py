import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

href = soup.select("[href^='https://']")
print(href)
