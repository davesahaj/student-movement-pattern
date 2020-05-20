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

    for x in s:
        df1 = pd.read_csv(x)
        df.merge(df1, left_on='Wifi Id', right_on='Wifi Id')


    

    fname = "data/visual/file-Sheet"+str(i)+".csv"
    df.to_csv(fname, index=None)
 

group1 = [6, 7, 8, 9, 10]
group2 = [3, 4, 5, 14, 16, 19, 20, 21]
group3 = [2, 13, 11, 15]

visual(group1)
visual(group2)
visual(group3)
