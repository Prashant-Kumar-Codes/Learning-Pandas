import pandas as pd

employee_data = {
    'id' : [i for i in range(101, 121)],
    
    'name' : ['Aman', None, 'Sahil', 'Kunal', 'Neha', 'Anjali', 'Priya', None,'Arjun', 'Vikas', 'Pooja', 'Nikhil', 'Nishant', 'Riya', None, 'Karan', 'Isha', 'Ramesh', 'Suresh', 'Pankaj'],
    
    'salary' : [35000, None, 58000, 61000, None, 53000, 69000, 76000, 48000, 55000, 62000, 71000, 39000, 46000, 84000, 90000, 67000, 52000, None, 74000 ],
    
    'department' : ['Software Development', None, 'Artificial Intelligence', 'Machine Learning', 'Cloud Computing', 'Cyber Security', 'IT Support', 'Network Engineering', 'DevOps', 'Quality Assurance', None, 'Business Analysis', None, 'Web Development', 'Mobile App Development', 'Database Administration', 'System Administration', 'IT Consulting', 'Technical Support', 'Enterprise Applications'],
    
    'workHours' : [7, None, 9, 6, 10, None, 7, 9, 8, 6, 10, 7, 9, 8, 6, 7, 10, None, 8, 7]
}


df = pd.DataFrame(employee_data)
print(df)

'''
1) Methods mainly used to CHECK missing data
--------------------------------------------
    isna()        / isnull()     → returns True for missing values in form of dataframe
    notna()       / notnull()    → returns True for non-missing values
    info()                        → shows non-null count per column
    missingno() (library)        → visual inspection

    Common usage:
        df.isna()
        df.isna().sum()
        df.info()
'''

print('\nisna() function:\n', df.isna())
print('\nisna() function:\n', df.notna())
print('\nisnull() function:\n', df.isnull())
print('\nisna().sum function:\n', df.isna().sum())
print('\ninfo() function:\n', df.info())





