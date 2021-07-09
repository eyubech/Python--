import pandas as pd
df = pd.read_csv('pokemon_data.csv')

df.columns

# Read each column
#print(df[['Name', 'Type 1', 'HP']])


# Read each row
for index, row in df.iterrows():
    print(index, row['Type 1'])