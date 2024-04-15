import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Creating sample data
np.random.seed(42) # Setting seed for reproducibility
data=np.random.randint(1, 10, 100) #Random integer values between 1 and 10
categories = ['London System', 'Caro kann', 'Sicilian defence', 'Scandinavian defence']
category_counts=np.random.randint(10, 50, len(categories)) # Random counts for each category.

# Plotting histogram.
plt.figure(figsize=(10, 6))
plt.hist(data, bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# Plotting bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, category_counts, color='lightgreen') 
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Counts')
plt.show()

# Plotting pie chart plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=categories, autopct='%1.1f%%',
colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen']) 
plt.title('Pie Chart')
plt.show()