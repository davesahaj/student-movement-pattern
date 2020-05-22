import pandas as pd
import seaborn


def get_dom(dt):
    return dt.day


def get_weekday(dt):
    return dt.weekday()


def get_hour(dt):
    return dt.hour


def get_minute(dt):
    return dt.minute


def converter(group):
    for i in group:
        print("creating sheet-"+str(i))
        fname = "data/csv/file-Sheet"+str(i)+".csv"
        df = pd.read_csv(fname)
        df.rename(columns={df.columns[2]: "Time"}, inplace=True)

        dates = []
        time = []

        for t in df.Time:
            t = t[0:8]
            time.append(t)

        for d in df.Date:
            d = d[0:10]
            dates.append(d)

        df['Date'] = dates
        df['Time'] = time

        df['Date'] = df[['Date', 'Time']].agg(' '.join, axis=1)

        fname = "data/trimmed/file-Sheet"+str(i)+".csv"

        df['Date'] = df['Date'].map(pd.to_datetime)
        df['weekday'] = df['Date'].map(get_weekday)
        df['dom'] = df['Date'].map(get_dom)
        df['hour'] = df['Date'].map(get_hour)
        df['minute'] = df['Date'].map(get_minute)
        df['Student ID'] = i

        df.sort_values(by=['Date'])
        df.to_csv(fname, columns=["Date", "Wifi Id",'Student ID'], index=None)


group1 = [1,2,3,4,5,6,7,8,9,10
,11,12,13,14,15,16,17,18,19,20
,21,22,23,24,25,26,27,28,29,30
,31,32,33,34,35,36,37,38,39,40
,41,42,43,44,45,46,47,48,49,50]

converter(group1)