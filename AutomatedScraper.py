import requests
import os.path
import pandas as pd

from config import fullUrl
from bs4 import BeautifulSoup


def main():

    response = requests.get(fullUrl)

    data = response.text
    soup = BeautifulSoup(data, features="lxml")

    titleResults = soup.findAll("a", class_="result-title hdrlnk")
    priceResults = soup.findAll("span", class_="result-price")
    dateResults = soup.findAll("time", class_="result-date")
    # urlResults = [x["href"] for item in soup.find_all("a", class_="result-title hdrlnk", attrs={'href': True})]

    urlResults = []
    for x in soup.find_all("a", class_="result-title hdrlnk", attrs={"href": True}):
        urlResults.append(x["href"])

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

    combined = list(zip(x.titles, x.prices, x.dates, x.urls))
    df_results = pd.DataFrame(combined, columns=["Title", "Price", "Posted", "URL"])

    exportPath = os.path.expandvars("/Users/$USER/Documents/results.csv")
    df_results.to_csv(exportPath)


if __name__ == '__main__':
    main()
