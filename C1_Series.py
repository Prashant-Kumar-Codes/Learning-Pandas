import pandas as pd

'''
Series: a one-dimensional labeled array in pandas.
        It is mainly used to store and operate on single-column or single-feature data.

------------------------------------------------
Creation Syntax
------------------------------------------------
    pd.Series(data, index=None, dtype=None, name=None)

------------------------------------------------
Parameters
------------------------------------------------
    data     - data source
               • list
               • tuple
               • dictionary
               • NumPy array
               • scalar value
    index    - labels for data (optional)
    dtype    - data type (optional)
    name     - name of the Series (optional)

------------------------------------------------
What it Contains
------------------------------------------------
    - Values → actual data
    - Index  → labels for each value
    - Name   → optional identifier

------------------------------------------------
Examples
------------------------------------------------
    From list:
        s = pd.Series([10, 20, 30])

    From dictionary:
        s = pd.Series({'a': 1, 'b': 2})

------------------------------------------------
Commonly Used Attributes
------------------------------------------------
    s.shape     → (n,)
    s.size      → number of elements
    s.index     → index labels
    s.values   → NumPy array of values
    s.dtype    → data type

------------------------------------------------
Commonly Used Methods
------------------------------------------------
    s.head()
    s.tail()
    s.info()
    s.describe()
    s.sort_values()
    s.drop()
    s.fillna()
    s.map()
    s.apply()

------------------------------------------------
Indexing & Selection
------------------------------------------------
    Label-based:
        s['a']

    Position-based:
        s.iloc[0]

    Boolean indexing:
        s[s > 10]

------------------------------------------------
Important Points
------------------------------------------------
    - Supports heterogeneous data types (object dtype)
    - Index makes Series more powerful than NumPy arrays
    - Arithmetic operations are index-aligned
    - A single column of DataFrame is a Series
    - Acts as the building block of DataFrame

------------------------------------------------
Professional Usage
------------------------------------------------
    - Feature columns in ML
    - Time-series data
    - Data cleaning and transformations
    - Mapping and value replacement
    - Statistical analysis

'''


pdSeries = pd.Series([10,20,30,40])
print(pdSeries,type(pdSeries))

pdSeries1 = pd.Series([10,20,30,40], index=['ten','twenty','thirty','fourty'])
print(pdSeries1, type(pdSeries1))

try:
    print(pdSeries == pdSeries1)
except:
    print('Cannot be compared')

# Important Attributes
    # s.index
    # s.values
    # s.dtype
    # s.shape
    # s.size

print(f'index: {pdSeries.index}\tvalues: {pdSeries.values}, {type(pdSeries.values)}\tdtype: {pdSeries.dtype}\tshape: {pdSeries.shape}\tsize: {pdSeries.size}')