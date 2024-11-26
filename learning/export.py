import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David',"Deepti"],
    'Age': [24, 30, None, 22,2],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York',"India"]
}
df = pd.DataFrame(data)

# Exploring the DataFrame
print(df.head())
print(df.isnull().sum())

# Cleaning the data
df.fillna(value={'Age': df['Age'].mean()}, inplace=True)

# Grouping by City and calculating the mean age
mean_age = df.groupby('City')['Age'].mean()
print(mean_age)

# Exporting to CSV
df.to_csv('cleaned_data.csv', index=False)
