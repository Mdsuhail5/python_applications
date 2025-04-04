from bs4 import BeautifulSoup
import lxml     # sometimes html.parser doesnt work on certain websites so use lxml
with open("", ) as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title)  # gets the title tag of the html page
print(soup.title.string)  # gets just the string of the title

print(soup)
print(soup.prettify())
print(soup.a)  # gets anchor tag

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)  # prints the anchor tags

for tag in all_anchor_tags:
    print(tag.getText())     # gets all the anchor tags
    print(tag.get("href"))  # gets all the links without any tags


heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get())


# to narrow down to a particular element
company_url = soup.select_one(selector="p a")  # css selector using the tags
print(company_url)


company_url = soup.select_one(selector="#name")  # id
print(company_url)

headings = soup.select(".heading")  # class
print(headings)
