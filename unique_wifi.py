import pandas as pd


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

            

        new_df.to_csv(fname, columns=[
                      "Date", "Wifi Id", "weekday", "dom", "hour", "minute"], index=None)



group1 = [6, 7, 8, 9, 10]
group2 = [3, 4, 5, 14, 16, 19, 20, 21]
group3 = [2, 13, 11, 15]

counter(group1)
counter(group2)
counter(group3)
