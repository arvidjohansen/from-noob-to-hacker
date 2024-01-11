from dataclasses import dataclass

@dataclass
class Person:
    age: int
    height: float
    weight: float

# Step 1: Create the data

import numpy as np
import pandas as pd

# Set a seed for reproducibility
np.random.seed(0)

# Generate correlated age and height data
age = np.random.normal(40, 10, 1000)
height = age / 2 + np.random.normal(0, 5, 1000)

# Generate uncorrelated weight data
weight = np.random.normal(70, 10, 1000)

# Create a DataFrame
df = pd.DataFrame({
    'age': age,
    'height': height,
    'weight': weight
})

# Convert the DataFrame to a list of Person objects
people = [Person(row['age'], row['height'], row['weight']) for _, row in df.iterrows()]


# Step 2: Display the data
import matplotlib.pyplot as plt
import seaborn as sns

# Create a pairplot of the data
sns.pairplot(df)

# Show the plot
plt.show()


# Calculate the correlation matrix
correlation_matrix = df.corr()

print("The correlation matrix is:")
print(correlation_matrix)