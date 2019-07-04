import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
#requests

webpage_response = requests.get("https://s3.amazonaws.com/codecademy-" +
                                "content/courses/beautifulsoup/shellter.html")
webpage = webpage_response.content
#print(webpage)

#TheBeautifulSoupObject

soup = BeautifulSoup(webpage, 'html.parser')
print(soup)

#ObjectTypes
print(soup.p)
print(soup.p.string)

#Navigating by Tags
for child in soup.div:
    print(child)

#Find All

# ##Using Regex
# soup.find_all(re.compile("[ou]l"))
# soup.find_all(re.compile("h[1-9]"))
# ##Using Lists
# soup.find_all(['h1', 'a', 'p'])
# ##Using Attributes
# soup.find_all(attrs={'class': 'banner'})
# soup.find_all(attrs={'class': 'banner', 'id': 'jumbotron'})
# ##Using Functions
#
#
# def has_banner_class_and_hello_world(tag):
#     return tag.attr('class') == "banner" and tag.string == "Hello world"
#
#
# soup.find_all(has_banner_class_and_hello_world)

turtle_links = soup.find_all('a')
print(turtle_links)

#Select for CSS Selectors and Reading text
links = []
for a in turtle_links:
    links.append(prefix+a["href"])

turtle_data = {}

for link in links:
    webpage = requests.get(link)
    turtle = BeautifulSoup(webpage.content, "html.parser")
    turtle_name = turtle.select(".name")[0]
    turtle_data[turtle_name] = [turtle.find("ul").get_text("|").split("|")]
print(turtle_data)

turtle_df = pd.DataFrame.from_dict(your_dictionary, orient='index')
