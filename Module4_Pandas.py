import pandas as pd

# Reading a CSV:

example = pd.read_csv("Random_Data.csv") # Between the "" must be located the file path
print(example)

# Create a series 
# A Series is a one-dimensional labeled array in Pandas. It can be thought of as a single column of data with labels or indices for each element.
data = [10,20,30,40,50]
s = pd.Series(data)
print(s)
# Accessing by position to a series. You can access elements in a Series using the index labels or integer positions. 
print("Accessing by location:\t" ,s.iloc[3])
print("Accessing by range:\t", "s[1:4]")  # Access a range of elements by label

                                ## Attributes and methods
                                            # values: Returns the Series data as a NumPy array. 
                                            # index: Returns the index (labels) of the Series.
                                            # shape: Returns a tuple representing the dimensions of the Series. 
                                            # size: Returns the number of elements in the Series.
                                            # mean(), sum(), min(), max(): Calculate summary statistics of the data. 
                                            # unique(), nunique(): Get unique values or the number of unique values. 
                                            # sort_values(), sort_index(): Sort the Series by values or index labels. 
                                            # isnull(), notnull(): Check for missing (NaN) or non-missing values. 
                                            # apply(): Apply a custom function to each element of the Series.

# Creating a DataFrame from a dictionary 
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],'Age': [25, 30, 35, 28],'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data) 
print(df)

# You can select a single column from a DataFrame by specifying the column name within double brackets. 
# Multiple columns can be selected in a similar manner, creating a new DataFrame.

print ("\n\n\nAccess the ID column")
print(example['ID']) # Access the ID column

# You can access rows by their index using .iloc[] or by label using .loc[].
print("\n\n")
print("Access the third row by position\t",df.iloc[2])   # Access the third row by position 
print("Access the second row by label\t",df.iloc[1])    # Access the second row by label
# Use the unique method to determine the unique elements in a column of a DataFrame.
unique_dates = df['Age'].unique()
print(unique_dates)

# You can filter data in a DataFrame based on conditions using inequality operators. For instance, you can filter albums released after a certain year.
high_above_102 = df[df['Age'] > 25]

# To save a DataFrame to a CSV file, use the to_csv method and specify the filename with a “.csv” extension.
# Pandas provides other functions for saving DataFrames in different formats.

df.to_csv('trading_data.csv', index=False)

