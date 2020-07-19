import pandas as pd
import os

sheets = []
i = 1
while i <= 50:
    sheets.append("data/counted/file-Sheet"+str(i)+".csv")
    i = i+1

df = pd.read_csv(sheets[0])
itrfile = iter(sheets)
next(itrfile)

for x in sheets:
    print(x)
    df1 = pd.read_csv(x)
    df = df.append(df1)

df = df.replace(to_replace='"Hostel"', value='Hostel')
df = df.replace(to_replace='"CEP"', value='CEP')
df = df.replace(to_replace='"LAB"', value='LAB')
df = df.replace(to_replace='"RC"', value='RC')
df = df.replace(to_replace='"Canteen"', value='Canteen')
df = df.replace(to_replace='"LT"', value='LT')

writer = pd.ExcelWriter('test.xlsx')
df.to_excel(writer, index=False)
writer.save()
