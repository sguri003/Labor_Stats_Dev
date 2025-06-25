import csv
import pandas as pd         
import numpy as np  
#altering
df_ky = pd.read_csv('BLS_API_KEY.csv')
print(df_ky['API'][0])
print(type(df_ky))
print(dict(df_ky).items)
dc = dict(df_ky)