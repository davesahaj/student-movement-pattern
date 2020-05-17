import pandas as pd
import numpy as np


def converter(group):
    for i in group:
        print("creating sheet-"+str(i))
        fname = "data/csv/file-Sheet"+str(i)+".csv"
        df = pd.read_csv(fname)
        df.rename(columns={df.columns[2]: "Time"}, inplace=True)

        dates = []
        time = []

        for d in df.Date:
            d = d[0:10]
            dates.append(d)

        for t in df.Time:
            t = t[0:5]
            time.append(t)

        df['Date'] = dates
        df['Time'] = time
        fname = "data/trimmed/file-Sheet"+str(i)+".csv"

        df.to_csv(fname, columns=["Date", "Time",
                                  "Wifi Id"], index=None, header=None)

group = [6, 7, 8, 9, 10]
converter(group)
