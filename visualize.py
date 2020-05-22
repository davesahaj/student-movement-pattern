import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import csv
import numpy as np


def visual(group):

    s = []
    for i in group:
        fname = "data/frequency/file-Sheet"+str(i)+".csv"
        s.append(fname)

    df = pd.read_csv(s[0])
    itrfile = iter(s)
    next(itrfile)

    frames = []

    for x in s:
        print(x)
        df1 = pd.read_csv(x)
        df = df.append(df1)

    fname = "data/visual/file-Sheet"+str(i)+".csv"

   # $count = df.groupby(['Wifi Id']).count()
    df.to_csv(fname,index=None)

   # df = pd.read_csv(fname)
  #  df.rename(columns={df.columns[1]: "Frequency"}, inplace=True)
   # df.drop(df[df.Frequency < 3].index, inplace=True)
   # df=df.sort_values(by=['Frequency'])
   # df.to_csv(fname)

    #df = pd.read_csv(fname)

   # x = df['Wifi Id']
   # y = df["Frequency"]
   # plt.bar(x, y, label="Example one", align='center', width=0.3)


#    plt.title('Most visited places')

    #plt.show()


group1 = [6, 7, 8, 9, 10]
group2 = [3, 4, 5, 14, 16, 19, 20, 21]
group3 = [2, 13, 11, 15]

visual(group1)
visual(group2)
visual(group3)
