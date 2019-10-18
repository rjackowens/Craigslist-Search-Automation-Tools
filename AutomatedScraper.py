from bs4 import BeautifulSoup
import requests

searchTerm = input("Enter search term: ")
minPrice = 175
maxPrice = 350


def url(search, min, max):
    return ("https://stlouis.craigslist.org/search/sss?sort=date&query=" + search + min + max)


response = requests.get(url(
    searchTerm,
    "&min_price=" + str(minPrice),
    "&max_price=" + str(maxPrice)
    ))

data = response.text
soup = BeautifulSoup(data, features="lxml")

titleResults = soup.findAll("a", class_="result-title hdrlnk")
priceResults = soup.findAll("span", class_="result-price")
dateResults = soup.findAll("time", class_="result-date")

urlResults = []
for x in soup.find_all("a", class_="result-title hdrlnk", attrs={"href": True}):
    urlResults.append(x["href"])

# value = [item['href'] for item in soup.find_all('a', class_="result-title hdrlnk", attrs={'href': True})]


class SoupParser:
    def __init__(self):
        self.titles = []
        self.prices = []
        self.dates = []
        self.urls = urlResults

    def getTitles(self, titles):
        for title in titles:
            self.titles.append(title.text)

    def getPrices(self, prices):
        for price in prices:
            self.prices.append(price.text)

    def getDate(self, dates):
        for date in dates:
            self.dates.append(date.text)


x = SoupParser()

x.getTitles(titleResults)
x.getPrices(priceResults)
x.getDate(dateResults)

combined = zip(x.titles, x.prices, x.dates, x.urls)

for title, price, date, url in combined:
    print(f"{title} | {price} | {date} \n {url}")

    
