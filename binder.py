import pandas as pd
import os

s = []
i = 1
while i <= 50:
    s.append("data/counted/file-Sheet"+str(i)+".csv")
    i=i+1

df = pd.read_csv(s[0])
itrfile = iter(s)
next(itrfile)

for x in s:
    print(x)
    df1 = pd.read_csv(x)
    df = df.append(df1)

writer = pd.ExcelWriter('test.xlsx')
df.to_excel(writer, index=False)
writer.save()
