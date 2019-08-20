from bs4 import BeautifulSoup
import requests
import lxml

def main():
    def search(x): return ("https://stlouis.craigslist.org/search/sss?sort=date&query=" + x)
    response = requests.get(search("bicycle"))
    data = response.text

    soup = BeautifulSoup(data, features="lxml")
    rawResults = soup.findAll("a", class_="result-title hdrlnk")

    for result in rawResults:
        print(result.text)

if __name__ == "__main__":
    main()
