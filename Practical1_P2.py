import pandas as pd
iris = pd.read_csv('iris[1].csv')

print("Original Iris dataset:")
print(iris.head())
#subset() function
#selecting only rows where species is versicolor
setosa_subset = iris[iris['species'] == 'versicolor']

print("\nSubset of Iris dataset with only 'versicolor' species:")
print(setosa_subset)
#aggregate() function to calculate mean sepal length for each species
aggregate_result = iris.groupby('species').agg({'sepal_length': 'mean'})

print("\nAggregate result - Mean sepal length for each species:")
print(aggregate_result)