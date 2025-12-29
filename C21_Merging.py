import pandas as pd

'''
merge(): combines two DataFrames based on common key column(s),
         similar to SQL JOIN operations.
         It is mainly used to combine related datasets.

Syntax
    pd.merge(left, right, on=None, how='inner')
    pd.merge(left, right, left_on=..., right_on=..., how='inner')

Parameters:
    left       - first DataFrame
    right      - second DataFrame
    on         - common column name(s) in both DataFrames
    left_on    - key column(s) from left DataFrame
    right_on   - key column(s) from right DataFrame
    how        - type of join:
                'inner', 'left', 'right', 'outer'
    suffixes   - suffixes for overlapping column names
    indicator  - adds column showing merge source
 
What it Does:
    - Joins rows from two DataFrames using key columns
    - Works like SQL JOIN
    - Matching is done by column values (not index by default)
    - Returns a new DataFrame
 

Why merge() exists:
    concat() → stacks data (rows/columns)
    join()   → index-based joining
    merge()  → column-based relational joining (most powerful)
 

Types of Merge (Very Important):

    1. Inner Join (default)
            pd.merge(df1, df2, on='id', how='inner')
            → Keeps only matching keys

    2. Left Join
            pd.merge(df1, df2, on='id', how='left')
            → Keeps all rows from left DataFrame

    3. Right Join
            pd.merge(df1, df2, on='id', how='right')
            → Keeps all rows from right DataFrame

    4. Outer Join
            pd.merge(df1, df2, on='id', how='outer')
            → Keeps all rows from both DataFrames
 
Examples:
    1. Simple merge on same column
            pd.merge(emp_df, dept_df, on='dept_id')

    2. Merge using different key names
            pd.merge(emp_df, dept_df,
        left_on='department_id',
            right_on='id')

    3. Merge with indicator column
            pd.merge(df1, df2, on='id', indicator=True)

    4. Handle duplicate column names
            pd.merge(df1, df2, on='id', suffixes=('_left', '_right'))


    For Index-based Merge:
        df1.merge(df2, left_index=True, right_index=True)
 
 
Important Points:
    - merge() does NOT modify original DataFrames
    - Key columns must have compatible data types
    - Default join is INNER
    - Row order may change after merge
    - NaN appears when no match is found
 

Common ML Use Cases
    ✔ Combining features from multiple tables
    ✔ Joining labels with feature sets
    ✔ Feature enrichment before training
    ✔ Data integration from multiple sources
 
Comparison:
    merge()  → relational join (columns)
    join()   → index-based join
    concat() → stacking data
    
Professional Tip:
    Use merge() when datasets are related
    through keys and relational logic is required.
 

'''
df_customers = pd.DataFrame({
    'cust_id' : [1,2,3,4,5],
    'cust_name' : ['Aman', 'Chaman', 'Raman', 'Agam', 'Pavan']
})

df_orders = pd.DataFrame({
    'cust_id' : [1, 2, 4, 1, 5 ,4, 1, 2],
    'amount' : [20000, 3333, 44444, 2222, 322243, 621, 5625, 30940]
})

#merging
df_merge = pd.merge(df_customers, df_orders, on = 'cust_id', how = 'inner')

print(df_merge['cust_id'].unique())
x = df_merge.groupby(['cust_id', 'cust_name', 'amount'])['cust_id'].unique()

print(x)