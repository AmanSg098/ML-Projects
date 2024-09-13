import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response = requests.get(url)

soup = BeautifulSoup(response.text,"lxml")

# extrecting the first header tag
tag = soup.header
# print(tag.attrs['role'])

# extracting the first p tag within first div tag
tag2 = soup.div.p
# print(tag2.string)

# extracting header tag
tag3 = soup.header.div.a.span
# print(tag3.string)

'''Note: if we manually select the tags from the html code such as
         (soup.div) or (soup.header.div) it will always extract 
         the first occurrance of that tag and if further
         child tags are mentioned it will only select the
         first occurrance of those tags on each level.'''

'''Similar functionality is shown by find() method of 
    BeautifulSoup for e.g.'''
tagFind = soup.find("header") # finds the first header tag
tagFinddiv = tagFind.find("div") # finds the first div tag
# print(tagFinddiv.a.span) # accessing the data inside the header.div tags

# accessing the innenr tags using class attribute of theirs
h4 = soup.find("h4",{"class":"price float-end card-title pull-right"})
# OR
desc = soup.find("p",class_ = "description")
# print(h4.string)
# print(desc.string)
# print(response)
# print(soup)

# extracting data from nested html tags
products = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")
# print(nestedtag)
# print(len(nestedtag))

# selecting any of the divs out of those 21 divs
product = products[2]
data = product.a
print(data.string)



