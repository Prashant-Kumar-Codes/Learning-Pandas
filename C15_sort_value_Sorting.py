import pandas as pd
from DataSets import df

'''
--------------------SORTING---------------------

sort :  arranges data in a specific order based on index or column values.
        It is mainly used to organize and analyze data efficiently.
------------------------------------------------

Functions Used:-
    sort_values()
    sort_index()

------------------------------------------------
'''
'''
1) sort_values(): sorts DataFrame or Series by values
------------------------------------------------
Syntax:
------------------------------------------------
    df.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort')

------------------------------------------------
Parameters:
------------------------------------------------
    by          - column name(s) to sort by
    axis        - 0 → sort rows (default)
                  1 → sort columns
    ascending   - True → ascending order
                  False → descending order
    inplace     - if True, modifies original DataFrame
    kind        - sorting algorithm ('quicksort', 'mergesort', 'heapsort')

------------------------------------------------
What it Does:
------------------------------------------------
    - Sorts data based on column values
    - Supports single or multiple columns
    - Preserves index unless reset

------------------------------------------------
Examples:
------------------------------------------------
    Sort by single column:
        df.sort_values(by='Age')

    Sort in descending order:
        df.sort_values(by='Marks', ascending=False)

    Sort by multiple columns:
        df.sort_values(by=['Age', 'Marks'], ascending=[True, False])

    Sort Series:
        s.sort_values()

------------------------------------------------
'''


df1 = df
df2 = df
print('Labels of dataframe:\n', df1.columns)

#sorted by single column
df1.sort_values(by = 'Name', ascending = True, inplace = True, ignore_index= True)
print('\nSorted dataframe by Name column\n\n', df1)

#sorting by multiple column
df2.sort_values(by = ['Name', 'Age'], ascending = [True, True], inplace = True)
print('\nSorted df2\n\n', df2)