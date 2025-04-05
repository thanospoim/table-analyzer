import requests
from bs4 import BeautifulSoup
import pandas as pd 
import matplotlib.pyplot as plt
url = 'https://el.wikipedia.org/wiki/%CE%A4%CE%BF_%CF%83%CF%8C%CE%B9_%CF%83%CE%BF%CF%85'
inp_table = int(input("which table want you to analyse?"))
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
soupp = soup.prettify()
with open('code.html','w',encoding='utf-8') as f:
    f.write(soupp)
tables = soup.find_all(class_='wikitable')[inp_table]
with open('code.txt','w',encoding='utf-8') as f:
    f.write(str(tables))
# Extract headers
headers = [th.text.strip() for th in tables.find_all("th")]

# Extract rows
rows = []
for tr in tables.find_all("tr")[1:]:
    cols = [td.text.strip() for td in tr.find_all(["td", "th"])]
    if cols:
        rows.append(cols)

# Convert to DataFrame
df_manual = pd.DataFrame(rows, columns=headers)


print(df_manual)




