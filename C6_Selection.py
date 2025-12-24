import pandas as pd

#NOTE: WHEN USING & AND | USE ( ) BECAUSE THESE BITWISE OPERATORS HAVE THE SECOND HIGHTEST PRECEDENCE WHILE COMPUTATION AND LEADS TO UNEXPECTED ERRORS

data = {
    'Name': ['Aman', 'Rohit', 'Sahil', 'Kunal', 'Neha', 'Anjali', 'Priya', 'Simran','Arjun', 'Vikas', 'Pooja', 'Nikhil','Riya', 'Sandeep', 'Karan', 'Isha'],
    'Age': [ 18, 19, 20, 21, 17, 19, 20, 18, 21, 22, 19, 20, 18, 23, 21, 19],
    'City':  ['Delhi', 'Mumbai', 'Chandigarh', 'Mohali', 'Ludhiana', 'Jaipur', 'Pune', 'Bengaluru', 'Noida','Gurugram', 'Delhi', 'Mumbai', 'Chandigarh', 'Mohali', 'Ludhiana', 'Ropar'],
    'Marks': [8.4, 7.9, 8.6, 7.5, 9.1, 8.2, 8.8, 7.6, 8.9, 7.8, 8.3, 8.7, 7.4, 8.1, 8.5, 9.0]
    }


df = pd.DataFrame(data)
print(f'Data Frame:\n{df}')


#---------------COLUMN SELECTION----------------

# selecting single column
print('\n\nName column (single column return series\n)')
nameCol = df['Name']    #argument is the column name
print(nameCol)

#selecting multiple columns
print('\n\nName and Age column (more that 1 column returns dataframe\n)')
nameAgeCol = df[['Name', 'Age']]    #argument is the list of column names
print(nameAgeCol)


#------------------ROW FILTER-----------------

#selecting data where Age is greater than 20
ageGreater20 = df[df['Age'] > 20]
print('\n\nAge greater than 20\n\n',ageGreater20)


#selecting data where age is less than 20 and Marks greater than 8.2
''' NOTE:
x = df[(df['Age'] < 20) and (df['Marks'] > 8.2)]    # WRONG

BECAUSE IT IS EVALUATED AS (Series and Series) but 'and' is logical operator and only wrongs for single True/False value either side not Seires of values
'''

x = df[(df['Age'] < 20) & (df['Marks'] > 8.2)]    # CORRECT
'''
THIS WORKS WELL BECAUSE:
    & is a bitwise AND operator
    Pandas overloads (&) to work element-wise on Series
    Each row is compared independently
    Internally it works like:

    True  & True  → True
    False & True  → False
    True  & False → False
'''
print('\n\nAge less than 20 and Marks greater than 8.2\n', x)

#selecting data where Age is > 20 OR Marks is > 8.2
y = df[(df['Age'] > 20) | (df['Marks'] > 8.2)]
print('\n\nAge greater than 20 or Marks greater than 8.2\n', y)
