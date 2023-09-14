import requests
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')  #lxml is a Python library which allows for easy handling of XML and HTML files, and can also be used for web scraping.
quotes = soup.find_all('span', class_='text')  # find all tags
authors = soup.find_all('small', class_='author')  # find all tags

tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print('--' + authors[i].text)
    tagsforquote = tags[i].find_all('a', class_='tag')
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    break