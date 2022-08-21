# import libraries

from bs4 import BeautifulSoup

# specify the url

# query the website and return the html to the variable ‘page’
import requests
page = requests.get("https://www.nike.com/ca/")

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.content, "html.parser")

# Take out the <div> of name and get its value
name_box = soup.find("h1", attrs={"class": "si35-ISy responsive-display-2-1 _2svRm8bR text-color-primary-dark"})

name = name_box.text.strip() # strip() is used to remove starting and trailing
print (name)

# get the index price
price_box = soup.find("div", attrs={"class": "cta-container Yjk73vve"})
price = price_box.text
print (price)

