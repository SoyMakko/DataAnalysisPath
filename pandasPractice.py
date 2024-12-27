import pandas as pd

# Create a dataframe as the image
a = {'Student': ['David','Samuel','Terry','Evan'], 'Age': [27,24,22,32], 
    'Country': ['UK','Canada', 'China', 'USA'],'Course': ['Python','Data Structures','Machine Learning','Web Development'],'Marks': [85,72,89,76]}

df = pd.DataFrame(a)

for i in df:
    print(df[i])


#Problem 2: Retrieve the Marks column and assign it to a variable b
b = df[['Marks']]
print(b)
# Problem 3: Retrieve the Country and Course columns and assign it to a variable c
c = df[['Country','Course']]
print(c)