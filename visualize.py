import pandas as pd
import dateutil
import os


def frequency(group):
    interval = [1, 2, 3, 4, 6, 8, 12]
    wifis = ['Canteen', 'Hostel', 'Event']
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

    df['Date'] = df['Date'].apply(dateutil.parser.parse, dayfirst=True)
    df = df.sort_values(by='Date')

    dates = []
    for d in df['Date'].dt.date:
        if d not in dates:
            dates.append(d)

    frame = pd.DataFrame()

    for x in dates:
        frame = frame.append(df.loc[df['Date'].dt.date == x])

    #frame.set_index('Student ID', inplace=True)
    frame = frame.sort_values(by='Student ID')

    for folder in wifis:
        if not os.path.exists("bin/"+folder):
            os.mkdir("bin/"+folder)
        
        
        final = pd.DataFrame(columns=['Date', 'Student ID', 'Frequency'])

        for d in dates:
            for s in group:
                fl = (frame.loc[frame['Wifi Id'] == '"'+folder+'"'])
                fl = (fl.loc[fl['Date'].dt.date == d])
                fl = (fl.loc[fl['Student ID'] == s])
                freq = fl.index
                freq = len(freq)

                final = final.append(
                    {'Date': d, 'Student ID': s, 'Frequency': freq}, ignore_index=True)


##############
        final.to_csv("bin/"+folder+"/"+str(folder)+".csv", index=None)


##############

   # frame = (frame.between_time(start_hour, end_hour))
   # frame = (frame.groupby('Wifi Id').count())
   # frame.to_csv("data/frequency/"+str(x)+".csv")

    # df.to_csv("out.csv")

group1 = [6, 7, 8, 9, 10]
group2 = [3, 4, 5, 14, 16, 19, 20, 21]
group3 = [2, 13, 11, 15]

if not os.path.exists("bin"):
    os.mkdir("bin")
frequency(group1)
# frequency(group2)
#frequency(group3)
