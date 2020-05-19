import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import csv 

fname = "data/trimmed/file-Sheet6.csv"
df = pd.read_csv(fname)

x = [1,2,3,4]
y = [1,4,9,16]


plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()