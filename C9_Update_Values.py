import pandas as pd
from DataSets import df

print('Data Frame:\n', df)


# Methods to update data in a Pandas DataFrame or Series

'''
------------------------------------------------
1. Direct Assignment Using loc[]
------------------------------------------------
Definition:
    Update values by assigning directly using labels or conditions.

Syntax:
    df.loc[row_label, column_label] = value
    s[index] = value

Examples:
    df.loc[0, 'Age'] = 25
    df.loc[df['Marks'] < 8, 'Marks'] = 8.0
    s[2] = 100
'''

df.loc[1, 'Name'] = 'Sunil Chetri'
print('\nData Frame after changing name:\n', df)



'''
------------------------------------------------
2. Conditional Assignment Using loc[]
------------------------------------------------
Definition:
    Update values using label-based indexing.

Syntax:
    df.loc[condition, column] = value

Examples:
    df.loc[df['Age'] > 20, 'City'] = 'Delhi'
'''

#df.loc[len(df['Name']) < 10, 'Name'] = df['Name']+str(10-len(df['Name']))      
# Wrong because len(df['Name']) give a single bool False (16 < 10) but need series of bool
df.loc[df['Name'].str.len() < 10, 'Name'] = df['Name'] + '(l)'
print('\nData Frame after adding number in Name:\n', df)

#increasing marks by 5%
#df.loc[df['Marks'] < 8, 'Marks'] += df['Marks'] * 0.05     #This works
df.loc[df['Marks'] < 8, 'Marks'] = df['Marks'] * 1.05       #This also works 
print('\nData Frame after increasing marks with 5%:\n', df)


'''
------------------------------------------------
3. Using iloc[]
------------------------------------------------
Definition:
    Update values using positional indexing.

Syntax:
    df.iloc[row_index, col_index] = value

Examples:
    df.iloc[0, 1] = 30

------------------------------------------------
4. Using at[] (Fast single value update)
------------------------------------------------
Definition:
    Fast label-based scalar update.

Syntax:
    df.at[row_label, column] = value

Examples:
    df.at[2, 'Marks'] = 9.5

------------------------------------------------
5. Using iat[] (Fast positional update)
------------------------------------------------
Definition:
    Fast positional scalar update.

Syntax:
    df.iat[row_index, col_index] = value

Examples:
    df.iat[1, 2] = 'Mumbai'

------------------------------------------------
6. Using replace()
------------------------------------------------
Definition:
    Replace specific values in DataFrame or Series.

Syntax:
    df.replace(old_value, new_value)
    df.replace({old: new})

Examples:
    df.replace(7.5, 8.0, inplace=True)
    s.replace(0, None, inplace=True)

------------------------------------------------
7. Using where()
------------------------------------------------
Definition:
    Update values where condition is False.

Syntax:
    df.where(condition, new_value)

Examples:
    df['Marks'] = df['Marks'].where(df['Marks'] >= 8, 8)

------------------------------------------------
8. Using mask()
------------------------------------------------
Definition:
    Opposite of where(); update values where condition is True.

Syntax:
    df.mask(condition, new_value)

Examples:
    df['Marks'] = df['Marks'].mask(df['Marks'] < 8, 8)

------------------------------------------------
9. Using apply()
------------------------------------------------
Definition:
    Update values using a function.

Syntax:
    df['column'] = df['column'].apply(function)

Examples:
    df['Marks'] = df['Marks'].apply(lambda x: x + 0.5)

------------------------------------------------
Important Points:
    - loc/iloc are preferred for conditional updates.
    - at/iat are fastest for single-cell updates.
    - replace/where/mask are safer for bulk updates.
    - apply is slower and should be used when logic is complex.

'''




