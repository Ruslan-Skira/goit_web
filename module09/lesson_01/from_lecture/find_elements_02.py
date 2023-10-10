import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

# Example 1знайти перший тег <p> на сторінці
first_paragraph = soup.find("p")
# print(first_paragraph)

# # Example 2 знайти всі теги <p> на сторінці
# all_paragraphs = soup.find_all("p")
# print(all_paragraphs)

# # Example 3 отримати текст першого тега <p> на сторінці
# first_paragraph_text = first_paragraph.get_text()
# print(first_paragraph_text.strip())  # 'Login'

# Example 4
# отримати значення атрибута "href" першого тегу <a> на сторінці
# first_link = soup.find("a")
# first_link_href = first_link["href"]
# print(first_link_href)  # '/'

# Example 5
body_children = list(first_paragraph.children)
# print(body_children)

# Example 6
# знайти перший тег <a> всередині першого тегу <div> на сторінці
first_div = soup.find("div")
first_div_link = first_div.find("a")
# print(first_div_link)

# Example 7
first_paragraph_parent = first_paragraph.parent
# print(first_paragraph_parent)

# Example 8
container = soup.find("div", attrs={"class": "quote"}).find_parent("div", class_="col-md-8")
print(container)