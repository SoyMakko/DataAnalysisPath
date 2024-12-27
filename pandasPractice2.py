import pandas as pd

df = pd.read_csv("TopSellingAlbums.csv")
print(df.head()) # Print first five rows of the dataframe

x = df[['Length']]
print(x)
y = df[['Artist','Length','Genre']]
print(y)


# Access the value on the first row and the first column
df.iloc[0, 0]

# Access the value on the second row and the first column
df.iloc[1,0]

# Access the value on the first row and the third column
df.iloc[0,2]

# Access the value on the second row and the third column
df.iloc[1,2]

# Access the column using the name
df.loc[1, 'Released']

# Slicing the dataframe
print("\nSliced\n",df.iloc[0:2, 0:3],"\n")

# Slicing the dataframe using name
print(df.loc[0:2, 'Artist':'Released'])