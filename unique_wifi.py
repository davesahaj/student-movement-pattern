import pandas as pd
import os

def counter(group):
    for i in group:
        print("creating sheet-counted-"+str(i))
        fname = "data/trimmed/file-Sheet"+str(i)+".csv"
        df = pd.read_csv(fname)
        fname = "data/counted/file-Sheet"+str(i)+".csv"

        new_df = pd.DataFrame(data=None, columns=df.columns)

        for i in range(1, df.shape[0]):
            rowSeries = df.iloc[i]
            nextRowSeries = df.iloc[i-1]
            if(rowSeries['Wifi Id'] != nextRowSeries['Wifi Id']):
                new_df = new_df.append(rowSeries)

        new_df.to_csv(fname, columns=["Date", "Wifi Id","Student ID"], index=None)


if not os.path.exists("data/counted"):
    os.mkdir("data/counted")

group1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
          26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

counter(group1)