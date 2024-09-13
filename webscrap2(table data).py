import requests
from bs4 import BeautifulSoup
import pandas as pd

# url for the site containing the table
url = "https://ticker.finology.in/market/index/bse/sensex"
response = requests.get(url)
# print(response)  # reponse 200
# print(response.text)  # checking for web sontent

# creating the soup object
soup = BeautifulSoup(response.text,"lxml")
# print(soup)  # ok

table = soup.find("table", class_ = "table table-sm table-hover screenertable")
# print(table)  # ok

# extracting the header row of the table
header = table.find_all("th", scope="col")
columns = [head.text for head in header]
# print(columns)   # ok

# extreacting the row data from the table
row_data = table.find_all("tr")
# running the loop skipping the first row(header row)
for row in row_data[1:]:
    # finding all the table data tags for the actual data
    data = row.find_all("td")
    # print(data)  # ok
    # storing the content of the data obtained in list
    row_content = [d.text for d in data]
    print(row_content)

# print(row_data)



