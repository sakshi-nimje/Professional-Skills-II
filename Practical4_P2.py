import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = pd.read_csv("iris[4].csv")
del df["Species"], df["Id"]
corr_mat = df.corr()
sb.heatmap(corr_mat, annot=True, cmap="coolwarm", fmt='.2f')
plt.title("Correlation Plot - Iris Dataset")
plt.show()