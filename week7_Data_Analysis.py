# =============================================
# Assignment: Data Analysis with Pandas & Matplotlib
# Author: Aaron Kimutai
# =============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Optional: set seaborn style for better visuals
sns.set(style="whitegrid")

# =============================================
# Task 1: Load and Explore the Dataset
# =============================================
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Iris dataset loaded successfully.\n")
except Exception as e:
    print(f"An error occurred: {e}")

# Display first 5 rows
print("First five rows of the dataset:")
print(df.head(), "\n")

# Check structure and missing values
print("Missing values in each column:")
print(df.isnull().sum(), "\n")

# =============================================
# Task 2: Basic Data Analysis
# =============================================
# Compute basic statistics for numerical columns
print("Basic statistics for numerical columns:")
print(df.describe(), "\n")

# Group by species and calculate mean of numerical columns
grouped = df.groupby('species', observed=True).mean()  # observed=True avoids FutureWarning
print("Mean of numerical columns grouped by species:")
print(grouped, "\n")

# =============================================
# Task 3: Data Visualization
# =============================================

# 1. Line plot: Trends of sepal length across samples
plt.figure(figsize=(8,5))
plt.plot(df['sepal length (cm)'], marker='o', linestyle='-', color='b')
plt.title('Line Plot of Sepal Length')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.show()

# 2. Bar chart: Average petal length per species using Matplotlib
plt.figure(figsize=(8,5))
plt.bar(grouped.index, grouped['petal length (cm)'], color=['#440154', '#21908C', '#FDE725'])
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)',
                hue='species', palette='Set1', s=100)
plt.title('Scatter Plot of Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# =============================================
# Findings / Observations
# =============================================
print("\nFindings / Observations:")
print("1. Setosa has smaller petal and sepal sizes compared to other species.")
print("2. Virginica shows the largest petal lengths and widths on average.")
print("3. Sepal width is fairly normally distributed.")
print("4. There is a strong positive correlation between sepal length and petal length.")
