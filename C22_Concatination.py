import pandas as pd

'''
concat(): combines multiple DataFrames or Series by stacking them
          along rows or columns.
          It is mainly used to append or join datasets vertically or horizontally.
 
Syntax:
    pd.concat(objs, axis=0)
    pd.concat(objs, axis=0, ignore_index=False)
    pd.concat(objs, axis=1)

Parameters:
    objs          - list or tuple of DataFrames / Series
    axis          - 0 → rows (vertical)
                    1 → columns (horizontal)
    ignore_index  - if True, resets index
    keys          - adds hierarchical index
    join          - 'outer' (default) or 'inner'
    sort          - sort non-concatenation axis (rarely needed)

What it Does: 
    - Stacks data along rows or columns
    - Does NOT match data like merge()
    - Index-based alignment (for axis=1)
    - Returns a new DataFrame or Series

Types of concat():
    Vertical concatenation (axis=0)
    Horizontal concatenation (axis=1)
 

Examples:
    Concatenate rows (same columns):
        pd.concat([df1, df2])

    Concatenate rows and reset index:
        pd.concat([df1, df2], ignore_index=True)

    Concatenate columns (side by side):
        pd.concat([df1, df2], axis=1)

    Concatenate Series into DataFrame:
        pd.concat([s1, s2], axis=1)

    Inner join on columns:
        pd.concat([df1, df2], join='inner')
 

For Series:
    pd.concat([s1, s2])


Important Points:
    - concat() stacks data, merge() matches data
    - Columns do NOT need a common key
    - Index matters when axis=1
    - Faster than merge() for simple stacking
    - Very common in data preprocessing
 
 
Professional Tip:
    Use concat() when datasets already align
    and you only need to stack or extend data,
    not perform relational joins.
 

'''

class1a = pd.DataFrame({
    'name' : ['Alpha', 'Beta', 'Gamma'],
    'marks' : [12, 15, 14]
})

class1b = pd.DataFrame({
    'name' : ['Theta', 'Delta'],
    'marks' : [19, 16]  
})

df_concat = pd.concat([class1a, class1b], axis=0, ignore_index=False)
print(df_concat)
df_concat1 = pd.concat([class1a, class1b], axis=0, ignore_index=True)
print(df_concat1)
df_concat2 = pd.concat([class1a, class1b], axis=1, ignore_index=False)
print(df_concat2)
df_concat3 = pd.concat([class1a, class1b], axis=1, ignore_index=True)
print(df_concat3)
df_concat4 = pd.concat([class1a, class1b], axis=1, ignore_index=True, join='inner')
print(df_concat4)
