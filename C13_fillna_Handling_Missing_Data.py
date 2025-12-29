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

'''
fillna(): replaces missing values (NaN / None) in a DataFrame or Series.
          It is mainly used to handle missing data without removing rows.

------------------------------------------------
Syntax
------------------------------------------------
    df.fillna({column : value}, inplace = False)    ## for pandas new version
    df.fillna({column1 : value, column2 = value}, inplace = False)
    df.fillna(value, inplace=False)     # in pandas old versions

------------------------------------------------
Parameters
------------------------------------------------
    column     - label name i.e. column name
    value      - value to replace NaN with
                 • scalar (single value)
                 • dictionary (column-wise values)
    inplace    - if True, modifies the original object

------------------------------------------------
What it Does
------------------------------------------------
    - Replaces only missing values (NaN / None)
    - Does NOT affect non-missing values
    - Preserves the shape of the DataFrame
    - Returns a new DataFrame unless inplace=True

------------------------------------------------
Examples
------------------------------------------------
    Fill all NaN values with 0:
        df1.fillna(0, inplace=True)

    Fill specific columns with default values:
        df.fillna({'name': 'Unknown', 'department': 'Unknown'}, inplace=True)

    Fill numeric column with mean value:
        df.fillna({'salary': int(df['salary'].mean())}, inplace=True)

------------------------------------------------
For Series
------------------------------------------------
    s.fillna(value)

------------------------------------------------
Important Points
------------------------------------------------
    - Works only on actual missing values (NaN / None)
    - Does NOT replace strings like 'None' or 'nan'
    - Dictionary-based fillna is professionally recommended
    - Preferred over dropna() when data loss is not acceptable
    - Safe and future-proof when applied directly on DataFrame
'''


# using fillna() function to fill the NaN values with some other values
# 1. filling with some default value
df.fillna(0, inplace = True)
print('\n\nAfter using fillna:\n', df)


# 2. filling specific column with default or mean value
#df1[['name', 'department']].fillna('Unknown', inplace = True)   ## wrong way due to new verison
df1.fillna({'name': 'Unknown', 'department': 'Unknown'}, inplace=True)

#df1['salary'].fillna(df1['salary'].mean().astype(int), inplace = True)   # working but do not prefer it
df1.fillna({'salary': int(df1['salary'].mean()), 'workHours': int(df1['workHours'].mean())}, inplace = True)
print('\n\nAfter using fillna on df:\n', df1)