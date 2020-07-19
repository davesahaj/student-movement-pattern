import pandas as pd
import dateutil
import os


def frequency(group):
    #   location,datetime, frequency
    wifis = ['Canteen', 'Hostel', 'CEP', 'LAB', 'RC', "LT"]
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

        final = pd.DataFrame(columns=['Frequency'])

        fl = (frame.loc[frame['Wifi Id'] == '"'+folder+'"'])
       # fl = (fl.loc[fl['Date'].dt.date == pd.to_datetime('2018-10-10')])
        fl = (fl.loc[(fl['Date'].dt.hour == 9) | (
            fl['Date'].dt.hour == 10) | (fl['Date'].dt.hour == 11)])
      #  fl = (fl.loc[fl['Student ID'] == s])
        freq = fl.index
        freq = len(freq)
        freq = (freq / 50)
        
        final = final.append(
            {'Frequency': freq}, ignore_index=True)

        final.to_csv("bin/"+folder+"/"+str(folder)+"9-10-11.csv", index=None)

##############
        final = pd.DataFrame(columns=['Frequency'])

        fl = (frame.loc[frame['Wifi Id'] == '"'+folder+'"'])
       # fl = (fl.loc[fl['Date'].dt.date == pd.to_datetime('2018-10-10')])
        fl = (fl.loc[(fl['Date'].dt.hour == 12) | (
            fl['Date'].dt.hour == 1) | (fl['Date'].dt.hour == 2)])
      #  fl = (fl.loc[fl['Student ID'] == s])
        freq = fl.index
        freq = len(freq)
        freq = (freq / 50)
        
        final = final.append(
            {'Frequency': freq}, ignore_index=True)

        final.to_csv("bin/"+folder+"/"+str(folder)+"12-1-2.csv", index=None)

##############
        final = pd.DataFrame(columns=['Frequency'])

        fl = (frame.loc[frame['Wifi Id'] == '"'+folder+'"'])
       # fl = (fl.loc[fl['Date'].dt.date == pd.to_datetime('2018-10-10')])
        fl = (fl.loc[(fl['Date'].dt.hour == 3) | (
            fl['Date'].dt.hour == 4) | (fl['Date'].dt.hour == 5)])
      #  fl = (fl.loc[fl['Student ID'] == s])
        freq = fl.index
        freq = len(freq)
        freq = (freq / 50)
        
        final = final.append(
            {'Frequency': freq}, ignore_index=True)

        final.to_csv("bin/"+folder+"/"+str(folder)+"3-4-5.csv", index=None)
#################
        final = pd.DataFrame(columns=['Frequency'])

        fl = (frame.loc[frame['Wifi Id'] == folder])
       # fl = (fl.loc[fl['Date'].dt.date == pd.to_datetime('2018-10-10')])
        fl = (fl.loc[(fl['Date'].dt.hour == 6) | (
            fl['Date'].dt.hour == 7) | (fl['Date'].dt.hour == 8)])
        #fl = (fl.loc[fl['Student ID'] == s])
        freq = fl.index
        freq = len(freq)
        freq = (freq / 50)
        final = final.append(
            {'Frequency': freq}, ignore_index=True)

        final.to_csv("bin/"+folder+"/"+str(folder)+"6-7-8.csv", index=None)
   # frame = (frame.between_time(start_hour, end_hour))
   # frame = (frame.groupby('Wifi Id').count())
   # frame.to_csv("data/frequency/"+str(x)+".csv")

    # df.to_csv("out.csv")


group1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
          26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]


if not os.path.exists("bin"):
    os.mkdir("bin")
frequency(group1)
# frequency(group2)
# frequency(group3)
