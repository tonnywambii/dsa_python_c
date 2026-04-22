import pandas as pd 
df = pd.read_excel("sales_2015_2020.csv")
#display the first five items 

print(df.head(5))

import os
print(os.getcwd())