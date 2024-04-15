import pandas as pd
df = pd.read_csv('iris[4].csv')
del df['Species'], df['Id']
print(df.corr())