from encodings import utf_8
from re import L
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import pandas as pd

df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])

link = 'https://stackoverflow.com'
df2 = pd.DataFrame([['a', 'a', 'a', 'd']],
                   index=[link],
                   columns=['a1', 'a2', 'a3', 'a4']
                   )
df3 = pd.DataFrame([['a', 'b', 'c', 'd']],
                   index=[link]
                   )

# print(df1)
print(df2)

with pd.ExcelWriter('output.xlsx', mode='a', if_sheet_exists="overlay") as writer:
    df2.to_excel(writer, sheet_name='Sheet3',)

with pd.ExcelWriter('output.xlsx', mode='a', if_sheet_exists="overlay") as writer:
    df3.to_excel(writer, sheet_name='Sheet3',
                 startrow=writer.sheets["Sheet3"].max_row, header=None)

# df1.to_excel("output.xlsx")
