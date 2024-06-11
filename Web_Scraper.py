from bs4 import BeautifulSoup
import requests

#Get HTML information from url
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#Seperate table from all other information
table = soup.find_all('table')[1]

#Seperate column titles from all other information
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

#Import into Panda Dataframe
import pandas as pd
df = pd.DataFrame(columns = world_table_titles)

#Seperate column data by row
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    #Appending each row to Panda DataFrame
    length = len(df)
    df.loc[length] = individual_row_data

#Print table and/or convert into csv file
print(df)
df.to_csv(r'/Users/cesardavila03/Documents/Coding Projects/Companies.csv', index = False)