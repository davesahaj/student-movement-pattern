import pandas as pd
import dateutil
import os


def frequency(group):
    #   location,datetime, frequency
    wifis = ['Canteen', 'Hostel', 'CEP', 'LAB', 'RC']
    start_hour = '09:00'
    end_hour = '12:00'
    s = []

    for i in group:
        s.append("data/counted/file-Sheet"+str(i)+".csv")
        # df['Date'] = df['Date'].apply(dateutil.parser.parse,dayfirst=True)

    df = pd.read_csv(s[0])
    itrfile = iter(s)
    next(itrfile)

    frames = []

    for x in s:
        print(x)
        df1 = pd.read_csv(x)
        df = df.append(df1)

    df['Date'] = df['Date'].astype('datetime64[ns]')

    for i in group:
        # fl = (df.loc[df['Student ID'] == i])
        fl = (df.loc[(df['Date'].dt.hour == 9) | (df['Date'].dt.hour == 10) | (df['Date'].dt.hour == 11)])
        fl = (fl.loc[fl['Wifi Id'] == '"'+"Canteen"+'"']) 

        fl.to_csv('out.csv',index=None)
    print(df)


group1 = [6, 7, 8, 9, 10]
group2 = [3, 4, 5, 14, 16, 19, 20, 21]
group3 = [2, 13, 11, 15]

if not os.path.exists("bin"):
    os.mkdir("bin")
frequency(group2)
# frequency(group2)
# frequency(group3)
