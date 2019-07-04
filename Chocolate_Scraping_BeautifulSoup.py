from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://s3.amazonaws.com/codecademy-" +
                       "content/courses/beautifulsoup/cacao/index.html")
webpage.encoding = 'utf-8'
soup = BeautifulSoup(webpage.content, 'html.parser')
print(soup)
ratings_tags = soup.find_all(attrs={"class": "Rating"})
ratings = []
for rating in ratings_tags:
    ratings.append(float(soup.find_all(attrs={"class": "Rating"})
                   [1].get_text()))

print(ratings_tags)
print(ratings)

plt.hist(ratings)
plt.show()
plt.clf()
company_tags = soup.select(".Company")
company_names = []
for name in company_tags:
    company_names.append(name.get_text())
data = {"Company": company_names, "Ratings": ratings}

best_chocolatier = pd.Dataframe.from_dict(data)

mean_vals = best_chocolatier.groupby("Company").Ratings.mean()

top_ten = mean_ratings.nlargest(10)

print(top_ten)

cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")

for tag in cocoa_percent_tags[1:]:
    percent = int(tag.get_text().strip('%'))
    cocoa_percents.append(percent)

best_chocolatier["CocoaPercentage"] = cocoa_percents

plt.scatter(best_chocolatier.CocoaPercentage, best_chocolatier.Rating)
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()
plt.clf()
