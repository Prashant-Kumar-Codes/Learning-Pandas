import pandas as pd
from DataSets import df

'''
2) sort_index(): sorts by index labels
------------------------------------------------
Syntax:
------------------------------------------------
    df.sort_index(axis=0, ascending=True, inplace=False)
    
------------------------------------------------
Parameters:
------------------------------------------------
    axis        - 0 → sort rows by index
                  1 → sort columns by index
    ascending   - True → ascending order
                  False → descending order
    inplace     - if True, modifies original DataFrame

------------------------------------------------
What it Does:
------------------------------------------------
    - Sorts based on index labels
    - Does NOT look at column values

------------------------------------------------
Examples:
------------------------------------------------
    Sort rows by index:
        df.sort_index()

    Sort columns alphabetically:
        df.sort_index(axis=1)

------------------------------------------------
Important Points:
------------------------------------------------
    - sort_values() → data-based sorting
    - sort_index()  → index-based sorting
    - Sorting returns a new object unless inplace=True
    - Often followed by reset_index()

'''

df1 = df
df2 = df

s = pd.Series([1, 2, 3, 'Hero', 'Shaktimaan', 'Ironman', 4, 5, 6, 'Thor', 'Wanda', 'Natasha'], index = ['num1', 'num2', 'num3', 'name1', 'name2', 'name3', 'num4', 'num5', 'num6', 'name4', 'name5', 'name6'])

print('Series:\n\n', s)
s.sort_index()
print('\n\nSorted series by sort_index:\n\n', s)
df1.sort_index(inplace=True)
df2.sort_index(axis=1, ascending=True, inplace = True)
print('\n\nSorted dataframe df1 by sort_index:\n\n', df1)
print('\n\nSorted dataframe df2 by sort_index:\n\n', df2)
