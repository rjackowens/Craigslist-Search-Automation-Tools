from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import lxml
import time

b = webdriver.Firefox()
b.get("https://stlouis.craigslist.org/")
b.implicitly_wait(2)

# Search for Item
search = b.find_element_by_xpath("//input[@id='query']")
search.click()
search.send_keys("Bicycle" + Keys.RETURN)

time.sleep(2) # Wait for results to load

# Sort Results by Date
select_dropdown = b.find_element_by_xpath("//div[@class='search-sort']")
select_dropdown.click()
select_date = b.find_element_by_xpath("//a[@data-selection='date']")
select_date.click()

page_source_results = b.page_source
soup = BeautifulSoup(page_source_results, features="lxml")
raw_results = soup.findAll("a", class_="result-title hdrlnk")

for result in raw_results:
    print(result.text)

b.quit()
