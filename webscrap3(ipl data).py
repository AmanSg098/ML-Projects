import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"
response = requests.get(url)
# checking the response
# print(response)  # ok 

# creating the soup  
soup = BeautifulSoup(response.text,"lxml")
# checking parsed text
# print(soup) # ok

table = soup.find("table",class_ = "ih-td-tab auction-tbl")
# checking parsed table
# print(table)  # ok

header = table.find_all("th", class_ = "skip-filter")
# checking parsed header from table
# print(header)  # ok
# extracting column names
column_name = [head.text for head in header]
# print(column_name)  # ok

data = table.find_all("tr")
# print(data)  # ok

df = pd.DataFrame(columns=column_name)
print(df)

for row in data[1:]:
    td = row.find_all("td")
    row_content = [d.text for d in td]
    # print(row_content)  # ok
    # adding rows to dataframe
    df.loc[len(df)] = row_content

print(df)


