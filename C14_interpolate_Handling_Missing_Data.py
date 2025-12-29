import pandas as pd

'''
interpolate(): fills missing values (NaN) by estimating them from surrounding data.
               It is mainly used for continuous or time-series data.

------------------------------------------------
Syntax
------------------------------------------------
    df.interpolate(method='linear', axis=0, inplace=False)

------------------------------------------------
Parameters
------------------------------------------------
    method     - technique to estimate values
                 • 'linear' (default)
                 • 'time'
                 • 'index'
                 • 'polynomial'
                 • 'nearest'
    axis       - 0 → column-wise
                 1 → row-wise
    inplace    - if True, modifies the original object

------------------------------------------------
What it Does
------------------------------------------------
    - Replaces NaN with calculated values
    - Uses nearby known values for estimation
    - Does NOT remove rows or columns
    - Best suited for ordered / numeric data

------------------------------------------------
Examples
------------------------------------------------
    Linear interpolation:
        df.interpolate(inplace=True)

    Interpolate using index values:
        df.interpolate(method='index')

    Time-based interpolation:
        df.interpolate(method='time')

    Polynomial interpolation (degree 2):
        df.interpolate(method='polynomial', order=2)

------------------------------------------------
For Series
------------------------------------------------
    s.interpolate()

------------------------------------------------
Important Points
------------------------------------------------
    - Works only on numeric data
    - Requires logical order in data
    - Not suitable for categorical/text columns
    - More meaningful than fillna() for time-series
    - Commonly used in sensor, stock, and signal data

'''

employee_data = {
    'id' : [101, None, 103, 104, 105, None, 107, 108, 109, 110, None, None, 113, 114, 115, 116, 117, 118, 119, 120],
    
    'name' : ['Aman', None, 'Sahil', 'Kunal', 'Neha', 'Anjali', 'Priya', None,'Arjun', 'Vikas', 'Pooja', 'Nikhil', 'Nishant', 'Riya', None, 'Karan', 'Isha', 'Ramesh', 'Suresh', 'Pankaj'],
    
    'age' : [24, None, 25, 22, 56, 32, None, 33, 23, 26, 28, 29, None, 44, 41, 20, None, 30, 36, 32],
    
    'salary' : [35000, None, 58000, 61000, None, 53000, 69000, 76000, 48000, 55000, 62000, 71000, 39000, 46000, 84000, 90000, 67000, 52000, None, 74000 ],
    
    'department' : ['Software Development', None, 'Artificial Intelligence', 'Machine Learning', 'Cloud Computing', 'Cyber Security', 'IT Support', 'Network Engineering', 'DevOps', 'Quality Assurance', None, 'Business Analysis', None, 'Web Development', 'Mobile App Development', 'Database Administration', 'System Administration', 'IT Consulting', 'Technical Support', 'Enterprise Applications'],
    
    'workHours' : [7, None, 9, 6, 10, None, 7, 9, 8, 6, 10, 7, 9, 8, 6, 7, 10, None, 8, 7]

}


df = pd.DataFrame(employee_data)
df1 = pd.DataFrame(employee_data)

#df.interpolate(method='linear', axis=0, inplace=False)
df['age'].interpolate(method = 'linear', axis = 0, inplace = True)
df[['id', 'workHours', 'salary']] = df[['id', 'workHours', 'salary']].interpolate().astype(int)

#df['id'] = df['id'].astype(int)
print(df)