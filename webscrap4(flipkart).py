import requests
from bs4 import BeautifulSoup
import pandas as pd

# creating a for loop for a particular number of pages to be extracted
# since the page link has just a difference of page number at the end.

# creating lists for all the data being scrapped from website
Product_Names = []
Product_Prices = []
Product_Descriptions = []
Product_Ratings = []

for i in range(1,6):   #number of loops can be increased as well
    url = "https://www.flipkart.com/search?q=mobiles%20under%2060000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    res = requests.get(url)
    # checking the response
    # print(res)  # ok

    soup = BeautifulSoup(res.text,"lxml")
    # parsing the html text using BeautifulSoup
    # print(soup)  # ok

    division = soup.find("div", class_ = "DOjaWF gdgoEp")
    # checking for the extracted div
    # print(division)  # ok

    # extracting the product names
    names = division.find_all("div", class_="KzDlHZ")
    # extracting the product prices
    prices = division.find_all("div", class_="Nx9bqj _4b5DiR")
    # extracting the product descriptions
    descriptions = division.find_all("ul", class_="G4BRas")
    # extracting the product ratings
    ratings = division.find_all("div", class_ = "XQDdHH")
    
    # finding minimum number of the products loaded per page
    n = min(len(names),len(prices),len(descriptions),len(ratings))

    # appending all the Product Specifications in their respective list
    for j in range(n):
        Product_Names.append(names[j].text )

    for j in range(n):
        Product_Prices.append(prices[j].text)
    
    for j in range(n):
        Product_Descriptions.append(descriptions[j].text)
    
    for j in range(n):
        Product_Ratings.append(ratings[j].text)

    print(len(Product_Names))
    print(len(Product_Prices))
    print(len(Product_Descriptions))
    print(len(Product_Ratings))  # ok

# creating a dataframe for products
df = pd.DataFrame({'Product_Names':Product_Names,'Product_Descriptions':Product_Descriptions,
                   'Product_Prices': Product_Prices,'Product_Ratings':Product_Ratings})
print(df)
