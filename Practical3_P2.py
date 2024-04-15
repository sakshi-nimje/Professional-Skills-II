import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')
plt.figure(figsize=(10, 6))
sns.boxplot(x='Duration', data=df,
flierprops=dict(markerfacecolor='red', marker='o', markersize=8))
plt.title('Box Plot with Outliers Highlighted')
plt.show()