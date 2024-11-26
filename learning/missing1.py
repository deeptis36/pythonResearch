import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, np.nan, 30, np.nan, 22],
    'City': ['New York', 'Los Angeles', np.nan, 'Chicago', 'New York']
}

df = pd.DataFrame(data)
print("Original DataFrame:")

print(df)

# Check for missing values
print("\nMissing Values Count:")
print(df.isnull().sum())

df_dropped_age = df.dropna(subset=['Age'])
print("\nDataFrame after dropping rows with missing 'Age':")
print(df_dropped_age)

