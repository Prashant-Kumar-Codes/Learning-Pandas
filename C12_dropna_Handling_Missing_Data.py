import pandas as pd

employee_data = {
    'id' : [i for i in range(101, 121)],
    
    'name' : ['Aman', None, 'Sahil', 'Kunal', 'Neha', 'Anjali', 'Priya', None,'Arjun', 'Vikas', 'Pooja', 'Nikhil', 'Nishant', 'Riya', None, 'Karan', 'Isha', 'Ramesh', 'Suresh', 'Pankaj'],
    
    'salary' : [35000, None, 58000, 61000, None, 53000, 69000, 76000, 48000, 55000, 62000, 71000, 39000, 46000, 84000, 90000, 67000, 52000, None, 74000 ],
    
    'department' : ['Software Development', None, 'Artificial Intelligence', 'Machine Learning', 'Cloud Computing', 'Cyber Security', 'IT Support', 'Network Engineering', 'DevOps', 'Quality Assurance', None, 'Business Analysis', None, 'Web Development', 'Mobile App Development', 'Database Administration', 'System Administration', 'IT Consulting', 'Technical Support', 'Enterprise Applications'],
    
    'workHours' : [7, None, 9, 6, 10, None, 7, 9, 8, 6, 10, 7, 9, 8, 6, 7, 10, None, 8, 7]
}


df = pd.DataFrame(employee_data)
df1 = pd.DataFrame(employee_data)
df2 = pd.DataFrame(employee_data)
df3 = pd.DataFrame(employee_data)
df4 = pd.DataFrame(employee_data)
df5 = pd.DataFrame(employee_data)
print(df)
'''
dropna(): removes rows or columns that contain missing values (NaN / None).
          It is mainly used to clean data by deleting incomplete records.

------------------------------------------------
Syntax
------------------------------------------------
    df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

------------------------------------------------
Parameters
------------------------------------------------
    axis       - 0 or 'index' → drop rows
                 1 or 'columns' → drop columns
    how        - 'any'  → drop if at least one NaN exists
                 'all'  → drop only if all values are NaN
    thresh     - minimum number of non-NaN values required to keep
    subset     - list of columns to consider for NaN check
    inplace    - if True, modifies the original DataFrame

------------------------------------------------
What it Does
------------------------------------------------
    - Removes rows or columns containing missing values
    - Permanently reduces data size
    - Returns a new DataFrame unless inplace=True

------------------------------------------------
Examples
------------------------------------------------
    Drop rows with any missing value:
        df.dropna(inplace=True)

    Drop rows only if all values are missing:
        df.dropna(how='all')

    Drop columns containing NaN:
        df.dropna(axis=1)

    Drop rows based on specific columns:
        df.dropna(subset=['name', 'salary'])

    Keep rows with at least 2 non-NaN values:
        df.dropna(thresh=2)

------------------------------------------------
For Series
------------------------------------------------
    s.dropna()

------------------------------------------------
Important Points
------------------------------------------------
    - Causes data loss (use carefully)
    - Useful when missing data is insignificant
    - Often used before model training
    - fillna() is preferred when data retention is important
    - Commonly paired with info() to inspect missing values

'''
# using dropna() function to delete the rows having NaN values
'''Use dropna() only when deleting is our intention or deleting the NaN rows will not cause any significant affect on our dataset'''

df.dropna(inplace = True)
print('\n\nAfter using dropna:\n', df)
print('\n\nChecking details of the dataframe:')
print(df.info())
print(df.shape)
