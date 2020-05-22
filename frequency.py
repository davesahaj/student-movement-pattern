import pandas as pd
import dateutil


def frequency(group):
    interval = [1, 2, 3, 4, 6, 8, 12]
    start_hour = '02:00'
    end_hour = '04:00'
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

    df['Date'] = df['Date'].apply(dateutil.parser.parse, dayfirst=True)
    df = df.sort_values(by='Date')

    dates = []
    for d in df['Date'].dt.date:
        if d not in dates:
            dates.append(d)

    for x in dates:
        frame = (df.loc[df['Date'].dt.date == x])
        frame.set_index('Date', inplace=True)
        frame = (frame.loc[frame['Wifi Id'] == '"Canteen"'])
       

       # frame = (frame.between_time(start_hour, end_hour))
       # frame = (frame.groupby('Wifi Id').count())
        frame.to_csv("data/frequency/"+str(x)+".csv")

    # df.to_csv("out.csv")


group1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
          26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]



group2 = [3, 4, 5, 14, 16, 19, 20, 21]
group3 = [2, 13, 11, 15]

frequency(group1)
# frequency(group1)
# frequency(group2)
# frequency(group3)
