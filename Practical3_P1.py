import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')
plt.figure(figsize=(10, 6))
sns.boxplot(x='Duration', data=df)
plt.title('Box Plot')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Duration', y='Calories', data=df)
plt.title('Scatter Plot')
plt.show()

