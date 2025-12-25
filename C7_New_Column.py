import pandas as pd
from DataSets import df

print(f'Columns of Data Frame:  {df.columns}')
print(f'Shape of the dataframe:  {df.shape}')
# THERE ARE TWO WAYS TO ADD NEW COLUMN IN THE DATAFRAME - 1. STRAIGHT FORWARD BY ASSIGNMENT, 2. USING INSERT METHOD


# 1. ADDING NEW COLUMN BY ASSIGNMENT

'''
Syntax:  dataframe['NEw_column_name'] =  data
         data in the form of list, series, array
'''

df['Roll_No'] = [i for i in range(1,17)]
print(f'\n\nDataframe after inserting Roll_No column:\n{df}')


# 2. ADDING NEW COLUMN BY INSERT METHOD

'''
insert(): inserts a new column into a DataFrame at a specified position.
          It is mainly used when you want to control the exact column order.

Syntax:
    df.insert(loc, column, value, allow_duplicates=False)

Parameters:
    loc                (int)   - position (index) where the column is inserted
    column             (str)   - name of the new column
    value              - data for the column (scalar, list, Series, array)
    allow_duplicates   (bool)  - allow duplicate column names (default: False)

What it Does:
    - Inserts a column at the given position.
    - Shifts existing columns to the right.
    - Modifies the DataFrame in-place.

Examples:
    Insert a column at position 1:
        df.insert(1, 'Grade', ['A', 'B', 'A', 'C'])

    Insert a column with same value:
        df.insert(0, 'Country', 'India')

    Insert using a Series:
        df.insert(2, 'Result', df['Marks'] > 8.0)

Important Points:
    - Raises error if column name already exists (unless allow_duplicates=True).
    - Cannot be used to update an existing column.
    - Preferred over assignment when column order matters.

'''


df.insert(3, 'Fee', df['Age'] * 1000)
print(f'\n\nDataframe after inserting Fee column:\n{df}')