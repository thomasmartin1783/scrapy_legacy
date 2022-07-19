import pandas as pd

links = [
    'https://0',
    'https://1',
    'https://2',
    'https://3',
    'https://4',
]

df = pd.DataFrame([['a', 'b', 'c', 'd']],
                  columns=['a1', 'a2', 'a3', 'a4']
                  )
df.to_excel("output.xlsx", sheet_name='Sheet3')


for i in range(0, 5):

    df3 = pd.DataFrame([['a', 'b', 'c', 'd']],
                       index=[links[i]],
                       columns=['a1', 'a2', 'a3', 'a4']
                       )
    with pd.ExcelWriter('output.xlsx', mode='a', if_sheet_exists="overlay") as writer:
        df3.to_excel(writer, sheet_name='Sheet3',
                     startrow=writer.sheets["Sheet3"].max_row, header=None)
