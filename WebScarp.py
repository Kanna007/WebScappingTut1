import requests
from parsel import Selector
import time


start = time.time()


# Crawling skidrowreloaded.com  to get image data and ordinary link

# GET request to a WEBPAGE you want
responce = requests.get('http://skidrowreloaded.com')

# scrapping done in next step by creating respont.txt which contain all the web page content
# by using parsel library  importing selector to extrat data to file

selector = Selector(responce.text)

# Extracting href attribute
# you must have some basic understanding of HTML tags and HTML tree Structure
# and Xpath implementation
href_links = selector.xpath('//a/@href').getall()

# Extracting img attributes
img_links = selector.xpath('//img/@src').getall()

# printing all our results

print("***********************************************************")
print(href_links)
print("***********************************************************")
print(img_links)
print("***********************************************************")

end =time.time()
print("time taken to GET DATA:", (end-start))

