import numpy as np
import pandas as pd
df = pd.read_csv('Concrete_Data.csv')
i = 1
while i < len(df.index):
    print((df.iloc[i,3])/(sum(df.iloc[i, 0:7])))
    i = i + 1