# iris_analysis.py

# ===============================
# Python Script for Data Analysis
# Dataset: Iris
# ===============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------

try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    
    # Convert to Pandas DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    print("Dataset loaded successfully!\n")
    
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Inspect the first few rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Check data types and missing values
print("Dataset info:")
print(df.info(), "\n")

print("Missing values per column:")
print(df.isnull().sum(), "\n")

# No missing values in Iris dataset, but if there were:
# df.fillna(method='ffill', inplace=True)

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------

print("Statistical summary of numerical columns:")
print(df.describe(), "\n")

# Group by species and compute mean of numerical columns
species_group = df.groupby('species').mean()
print("Average measurements per species:")
print(species_group, "\n")

# Observations:
# - Setosa has the smallest petal length and width
# - Virginica has the largest sepal and petal measurements
# - Versicolor is intermediate in size

# -------------------------------
# Task 3: Data Visualization
# -------------------------------

# Set Seaborn style
sns.set(style="whitegrid")

# 1️⃣ Line Chart: Petal length trend by sample index
plt.figure(figsize=(8, 5))
for sp in df['species'].unique():
    subset = df[df['species'] == sp]
    plt.plot(subset.index, subset['petal length (cm)'], marker='o', linestyle='-', label=sp)
plt.title("Petal Length Trend by Species")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# 2️⃣ Bar Chart: Average sepal width per species
plt.figure(figsize=(6, 5))
sns.barplot(x=species_group.index, y=species_group['sepal width (cm)'], palette='viridis')
plt.title("Average Sepal Width per Species")
plt.xlabel("Species")
plt.ylabel("Sepal Width (cm)")
plt.tight_layout()
plt.show()

# 3️⃣ Histogram: Distribution of petal length
plt.figure(figsize=(6, 5))
sns.histplot(df['petal length (cm)'], bins=15, kde=True, color='skyblue')
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4️⃣ Scatter Plot: Sepal length vs Petal length colored by species
plt.figure(figsize=(7, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep', s=80)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.tight_layout()
plt.show()

# -------------------------------
# Task 4: Findings / Observations
# -------------------------------

print("\nFindings and Observations:")
print("- Setosa is easily separable from other species based on petal length and width.")
print("- Versicolor and Virginica show some overlap in sepal and petal measurements.")
print("- Petal length is a strong feature for distinguishing species.")
print("- Sepal width varies less significantly between species compared to petal measurements.")
