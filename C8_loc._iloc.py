import pandas as pd
from DataSets import df

print('Data Frame:\n', df)

'''
loc(): label-based indexer used to access rows and columns by their labels.
       It is mainly used for selecting data using row and column names.

Syntax:
    df.loc[row_label, column_label]

Parameters:
    row_label      - label or list/slice of row labels
    column_label   - label or list/slice of column names

What it Does:
    - Selects data based on index labels.
    - Supports boolean conditions.
    - Slice end is inclusive.

Examples:
    df.loc[0]
    df.loc[0, 'Name']
    df.loc[:, 'Age']
    df.loc[1:3, ['Name', 'Marks']]
    df.loc[df['Age'] > 20, ['Name', 'City']]

Important Points:
    - Uses labels, not positions.
    - Supports boolean filtering.
    - Both row and column selection are optional.

'''

df.loc[1, 'Name'] = 'Sunil Chetri'
print('\nData Frame after changing name:\n', df)