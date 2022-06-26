import pandas as pd

xls = pd.ExcelFile(r"Sheet-3.xlsx")  # use r before absolute file path

# 2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis
sheetX = xls.parse(0)

var1 = sheetX['Column1'].astype('string')

# print(var1.dtypes)
# print(type(var1[0]))  # 1 is the row number.
# print(var1[0])
print(len(var1))
