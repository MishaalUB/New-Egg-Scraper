from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38"

# opens connection, downloads html page from url
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# parses html
page_soup = soup(page_html, "html.parser")

# grabs each video card
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

contain = containers[0]
container = containers[0]

# loops this code for all products on the website
for container in containers:
	brand = container.div.div.a.img["title"]
	# Finds the 'a' tag with class of item-title for Product Name and then selects only text
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	# Finds 'li' tag with class of price-ship for Shipping and then selects only clean text
	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping: " + shipping)

	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()
