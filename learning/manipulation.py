import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

df = pd.read_csv('/home/preeti/Downloads/us-500.csv')
# print(df.head())
city = df['city']
county = df['county']
subset = df[['county', 'city']]

# print(subset)

row_1 = df.iloc[1]
# print(row_1)
# print(county)
cityGrouped = df.groupby('city')['zip'].mean()
print(cityGrouped)