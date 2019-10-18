regionUrl = "https://stlouis.craigslist.org/search/sss?sort=date&query="
searchTerm = "bike"
minPrice = "&min_price=" + str(100)
maxPrice = "&max_price=" + str(175)
fullUrl = regionUrl + searchTerm + minPrice + maxPrice
