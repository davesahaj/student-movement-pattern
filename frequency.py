import pandas as pd


def counter(group):
    for i in group:
        print("creating sheet-counted-"+str(i))
        fname = "data/counted/file-Sheet"+str(i)+".csv"
        df = pd.read_csv(fname)
        fname = "data/frequency/file-Sheet"+str(i)+".csv"

        count = df.groupby(['Wifi Id']).size()
       # count = 

        print(count)
        count.to_csv(fname)

        df = pd.read_csv(fname)
        df.rename(columns={df.columns[1]: "Frequency"}, inplace=True)
        df.to_csv(fname)



group1 = [6, 7, 8, 9, 10]
group2 = [3, 4, 5, 14, 16, 19, 20, 21]
group3 = [2, 13, 11, 15]

counter(group1)
counter(group2)
counter(group3)
