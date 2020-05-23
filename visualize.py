import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import csv
import os
import glob


def visual():
    location = 'bin/'

    folderset = [folder for folder in glob.glob(
        location + "**/", recursive=True)]

    for folder in folderset:
        files = (glob.glob(folder+"/*.csv"))


    df = pd.read_csv(files[0])
  #  df.rename(columns={df.columns[1]: "Frequency"}, inplace=True)
   # df.drop(df[df.Frequency < 3].index, inplace=True)
   # df=df.sort_values(by=['Frequency'])
   # df.to_csv(fname)

    #df = pd.read_csv(fname)

   # x = df['Wifi Id']
   # y = df["Frequency"]
   # plt.bar(x, y, label="Example one", align='center', width=0.3)


#    plt.title('Most visited places')

    # plt.show()


visual()
