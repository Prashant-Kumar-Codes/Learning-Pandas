import pandas as pd
#   shape, size, columns are attributes not methods
'''-----------SHAPE--------------
shape: returns the dimensions of the DataFrame or Series.
       It is mainly used to know the number of rows and columns.

Syntax:
    df.shape

Parameters:
    None

What it Returns:
    A tuple in the form:
        (number_of_rows, number_of_columns)

    For Series:
        (number_of_elements,)

Examples:
    df.shape
        Output: (5, 3)   # 5 rows and 3 columns

    s.shape
        Output: (5,)     # Series with 5 elements

Important Points:
    - It is an attribute, not a function (no parentheses).
    - It does not count missing values separately.
    - Useful for quickly checking dataset size.

'''
'''----------SIZE--------------
size: returns the total number of elements (values) present in a DataFrame or Series.
      It is mainly used to know how much data exists in total.

Syntax:
    df.size

Parameters:
    None

What it Returns:
    An integer value equal to:
        number_of_rows x number_of_columns

    For Series:
        total number of elements

Examples:
    df.size
        Output: 12   # if DataFrame has 4 rows and 3 columns

    s.size
        Output: 5    # Series with 5 elements

Important Points:
    - It is an attribute, not a function (no parentheses).
    - It counts all elements, including missing values (NaN).
    - Useful when you need the total number of values, not the structure.

'''
'''-----------COLUMNS--------------
columns: returns the column labels (names) of a DataFrame.
         It is mainly used to identify, access, or modify column names.

Syntax:
    df.columns

Parameters:
    None

What it Returns:
    A Pandas Index object containing column names.

Examples:
    df.columns
        Output: Index(['Name', 'Age', 'City'], dtype='object')

    Access a single column name:
        df.columns[0]

    Rename all columns:
        df.columns = ['A', 'B', 'C']

    Convert column names to a list:
        list(df.columns)

Important Points:
    - It is an attribute, not a function (no parentheses).
    - Applicable only to DataFrames (not Series).
    - Useful for column selection, renaming, and inspection.

'''




dataFrame1 = pd.read_excel('Project_dataset.xlsx')
dataFrame2 = pd.DataFrame(
    {
        'Name': ['Prashat', 'Raj', 'Tushar', 'Abhisekh'],
        'Age': [18, 19, 19, 18],
        'City': ['Mohali', 'Delhi', 'Faridkort', 'Ropar']
    }
)

print(f'\nSize of dataFrame1: {dataFrame1.shape}')
print(f'\nSize of dataFrame1: {dataFrame1.size}')
print(f'\nColumn of dataFrame1: {dataFrame1.columns}')

print(f'\n\nSize of dataFrame1: {dataFrame2.shape}')
print(f'\nSize of dataFrame1: {dataFrame1.size}')
print(f'\nColumn of dataFrame1: {dataFrame2.columns}')

