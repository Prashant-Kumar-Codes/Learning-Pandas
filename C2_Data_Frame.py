import pandas as pd

'''
DataFrame: a two-dimensional, size-mutable, tabular data structure in pandas.
           It is mainly used to store and manipulate structured data
           (rows and columns, similar to an Excel sheet or SQL table).

------------------------------------------------
Creation Syntax
------------------------------------------------
    pd.DataFrame(data, index=None, columns=None, dtype=None)

------------------------------------------------
Parameters
------------------------------------------------
    data     - data source
               • dictionary
               • list of lists
               • list of dictionaries
               • NumPy array
               • Series
    index    - row labels (optional)
    columns  - column labels (optional)
    dtype    - data type for all columns (optional)

------------------------------------------------
What it Contains
------------------------------------------------
    - Rows → records / observations
    - Columns → features / attributes
    - Index → row labels
    - Each column is a pandas Series

------------------------------------------------
Examples
------------------------------------------------
    From dictionary:
        df = pd.DataFrame({
            'Name': ['Aman', 'Rohit'],
            'Age': [18, 19]
        })

    From list of lists:
        df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])

------------------------------------------------
Commonly Used Attributes
------------------------------------------------
    df.shape     → (rows, columns)
    df.size      → total number of elements
    df.columns   → column names
    df.index     → row index labels
    df.dtypes    → data types of columns

------------------------------------------------
Commonly Used Methods
------------------------------------------------
    df.head()
    df.tail()
    df.info()
    df.describe()
    df.sort_values()
    df.drop()
    df.fillna()
    df.loc[]
    df.iloc[]

------------------------------------------------
Important Points
------------------------------------------------
    - Heterogeneous data types are allowed
    - Column-wise operations are fast and optimized
    - Supports label-based and position-based indexing
    - Core data structure used in data analysis and ML pipelines
    - Acts as the foundation for most pandas operations

------------------------------------------------
Professional Usage
------------------------------------------------
    - Data cleaning
    - Data transformation
    - Exploratory data analysis (EDA)
    - Feature engineering
    - Preprocessing before ML models

'''


# dataframe
dict1 = {
    'column1_numbers': [1,2,3,4,5,6,7,8,9,10],
    'column2_alphabet':['a','b','c'],
    'column3_empty':[]
}

max_len = max(len(value) for value in dict1.values())

# print(max_len)

for key in dict1:
    for i in range(max_len - len(dict1[key])):
        if len(dict1[key]) < 10:
            dict1[key].append('NaN')
            
# print(dict1)
dict1_DataFrame = pd.DataFrame(dict1)
print(dict1_DataFrame)

dict1_DataFrame.to_csv('check1.csv', index=0)

print(len(dict1_DataFrame), type(dict1_DataFrame))
