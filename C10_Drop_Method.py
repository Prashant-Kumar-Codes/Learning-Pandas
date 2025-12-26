import pandas as pd
from DataSets import df

'''
drop(): removes specified rows or columns from a DataFrame or Series.
        It is mainly used to delete unwanted data.

------------------------------------------------
Syntax
------------------------------------------------
    df.drop(labels, axis=0, inplace=False, errors='raise')
    df.drop(columns=[column_name], inplace=False)

------------------------------------------------
Parameters
------------------------------------------------
    labels     - row index label(s) or column name(s) to remove
    axis       - 0 or 'index' → rows
                 1 or 'columns' → columns
    inplace    - if True, modifies the original object
    errors     - 'raise' (default) or 'ignore'

------------------------------------------------
What it Does
------------------------------------------------
    - Removes rows or columns by label.
    - Does NOT remove data by position.
    - Returns a new DataFrame/Series unless inplace=True.

------------------------------------------------
Examples
------------------------------------------------
    Drop a row:
        df.drop(2)

    Drop multiple rows:
        df.drop([1, 3, 5])

    Drop a column:
        df.drop('Age', axis=1)
        dfc2.drop(columns=['City'], inplace=True)   *****

    Drop multiple columns:
        df.drop(['Age', 'Marks'], axis=1)

    Drop using inplace:
        df.drop('City', axis=1, inplace=True)

    Ignore error if label not found:
        df.drop('Salary', axis=1, errors='ignore')

------------------------------------------------
For Series
------------------------------------------------
    s.drop(index_label)

------------------------------------------------
Important Points
------------------------------------------------
    - axis=0 → rows, axis=1 → columns
    - Use `columns=` for columns
    - Use `index=` for rows
    - Uses labels, not index positions
    - Original data remains unchanged unless inplace=True
    - Very commonly used during data cleaning


'''


dfc1 = df
dfc2 = df



print('Data Frame:\n', dfc1)


dfc1.drop(columns = ['City'])
print('\nUsing drop without inplace:\n', dfc1)

dfc2.drop(columns = ['City'], inplace = True)
print('\nUsing drop with inplace:\n', dfc2)

dfc2.drop(columns = ['Name', 'Age'], inplace = True)
print('\nUsing drop with inplace:\n', dfc2)