from bs4 import BeautifulSoup
import requests

searchTerm = input("Enter search term: ")
minPrice = input("Enter minimum price: ")
maxPrice = input("Enter maximum price: ")


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
priceResults = soup.find_all("span", class_="result-price")
dateResults = soup.find_all("time", class_="result-date")
# urlResults = soup.find_all("a", class_="data-id")


class SoupParser:
    def __init__(self):
        self.titles = []
        self.prices = []
        self.dates = []

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

combined = zip(x.titles, x.prices, x.dates)

for title, price, date in combined:
    print(f"{title} | {price} | {date}")

