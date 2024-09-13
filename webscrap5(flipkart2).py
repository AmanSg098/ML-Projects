import requests
from bs4 import BeautifulSoup
import pandas as pd

# getting the url
url = "https://www.flipkart.com/search?q=office%20tables%20under%2010000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

while True:
    print(url)  #ok
    res = requests.get(url)
    # checking the response from the website
    print(res)  # ok

    # creating the BeautifulSoup object 
    soup = BeautifulSoup(res.text,"lxml")
    # print(soup)  # ok

    # we will not using for loop here and will not pass numerical value to 
    # replace the page link instead we will update the link each time we are
    # on next page with the link in next page button
    nextpage = soup.find("a", class_ = "_9QVEpD").get("href")
    # print(nextpage)  # ok

    # completing the link
    cmpltnextpage = "https://www.flipkart.com" + nextpage
    # print(cmpltnextpage)  #ok

    # updating/ urls

    url = cmpltnextpage

