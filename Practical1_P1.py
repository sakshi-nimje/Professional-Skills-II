import pandas as pd
mtcars = pd.read_csv('mtcars[1].csv')
#Display summary statistics
print("Summary Statistics for mtcars dataset:")
print(mtcars.describe())
# Display structure information
print("\nStructure Information for mtcars dataset:")
print(mtcars.info())
#Display quartile information for numeric columns
numeric_columns = mtcars.select_dtypes(include=['number']).columns
print("\nQuartile Information for mtcars dataset:")
print(mtcars[numeric_columns].quantile([0.25, 0.5, 0.75]))

cars = pd.read_csv('cars[1].csv')
#Display summary statistics
print("\n\nSummary Statistics for cars dataset:")
print(cars.describe())
# Display structure information
print("\nStructure Information for cars dataset:")
print(cars.info())
#Display quartile information for numeric columns
numeric_columns = cars.select_dtypes(include=['number']).columns
print("\nQuartile Information for cars dataset:")
print(cars[numeric_columns].quantile([0.25, 0.5, 0.75]))