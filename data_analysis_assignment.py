# data_analysis_assignment.py

# 📦 Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# 🎯 Task 1: Load and Explore the Dataset

# Load the Iris dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    print("✅ Dataset loaded successfully.\n")
except Exception as e:
    print("❌ Error loading dataset:", e)

# Display the first few rows
print("🔍 First 5 rows of the dataset:")
print(df.head())

# Show info about data types and missing values
print("\n📊 Dataset Info:")
print(df.info())

# Check for missing values
print("\n❓ Missing Values:")
print(df.isnull().sum())

# No missing values in this dataset, but if there were:
# df.dropna(inplace=True)  # or df.fillna(...)

# 🎯 Task 2: Basic Data Analysis

# Basic statistics
print("\n📈 Descriptive Statistics:")
print(df.describe())

# Group by species (target) and compute mean values
print("\n📌 Mean values grouped by species:")
print(df.groupby('target').mean())

# Add species names for readability
df['species'] = df['target'].apply(lambda x: iris.target_names[x])

# 🎯 Task 3: Data Visualization

# Line Chart: Sepal and Petal Length Over Index
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.title("Sepal and Petal Length Over Sample Index")
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart: Average petal length per species
species_group = df.groupby('species')['petal length (cm)'].mean().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(data=species_group, x='species', y='petal length (cm)', palette='Set2')
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.tight_layout()
plt.show()

# Histogram: Sepal Width distribution
plt.figure(figsize=(8, 5))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Set1')
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.grid(True)
plt.tight_layout()
plt.show()

# 🧠 Findings and Observations:
print("\n🧠 Observations:")
print("- Setosa has smaller petal lengths compared to Versicolor and Virginica.")
print("- Petal length strongly correlates with sepal length.")
print("- Sepal width is approximately normally distributed.")
print("- Visualizations clearly separate species based on petal measurements.")
