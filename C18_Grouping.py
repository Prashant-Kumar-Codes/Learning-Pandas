import pandas as pd
from DataSets import empdf

'''
Grouping (groupby): used to split data into groups
                    based on one or more keys and
                    then apply aggregation or transformation.

------------------------------------------------
groupby():
------------------------------------------------
The groupby() operation follows **Split → Apply → Combine**:

1) Split the data into groups
2) Apply a function (sum, mean, etc.)
3) Combine the results

------------------------------------------------
Syntax:
------------------------------------------------
    df.groupby(by, axis=0, as_index=True, sort=True)

------------------------------------------------
Parameters:
------------------------------------------------
    by         - column name(s) or array to group by
    axis       - 0 (rows) [commonly used]
    as_index   - True → group keys become index
                 False → group keys remain columns
    sort       - whether to sort group keys

------------------------------------------------
What it Does
------------------------------------------------
    - Groups rows based on unique values
    - Does NOT change original data
    - Requires aggregation or transformation
    - Returns a GroupBy object (lazy evaluation)

------------------------------------------------
Basic Examples
------------------------------------------------
    Group by single column:
        df.groupby('City')

    Group by multiple columns:
        df.groupby(['City', 'Department'])
        
        
------------------------------------------------
Important GroupBy Methods
------------------------------------------------
    .sum()
    .mean()
    .median()
    .count()
    .min()
    .max()
    .std()
    .var()
    .nunique()
    .first()
    .last()

------------------------------------------------
GroupBy in Machine Learning
------------------------------------------------
Common ML use cases:
    - Feature engineering
    - Encoding categorical data
    - Statistical summaries per category

------------------------------------------------
Important Points
------------------------------------------------
    - groupby() itself does NOT compute
    - groupby() alone does nothing visible
    - Aggregation triggers computation
    - Ignores NaN values by default
    - Extremely important for EDA & ML
    - Prefer transform() when output
    - shape must match original DataFrame

'''


df = empdf
print(df.columns)
x = df.groupby('department')          
print(x)    # no output

# NOTE:  groupby() alone does nothing visible


'''
------------------------------------------------
Aggregation/Reduction methods with groupby()
------------------------------------------------
    Mean:
        df.groupby('City')['Salary'].mean()

    Sum:
        df.groupby('Department')['Marks'].sum()

    Multiple aggregations:
        df.groupby('City')['Salary'].agg(['mean', 'max', 'min'])

------------------------------------------------
Multiple Columns + Multiple Aggregations
------------------------------------------------
    df.groupby('City').agg({
        'Salary': ['mean', 'max'],
        'Age': 'median'
    })

------------------------------------------------
Keeping Group Column as Normal Column
------------------------------------------------
    df.groupby('City', as_index=False)['Salary'].mean()



------------------------------------------------
Transformation (same shape output)
------------------------------------------------
    df['City_avg_salary'] = df.groupby('City')['Salary'].transform('mean')

'''


# using single aggregation 
group_dep_sal_mean = df.groupby('department')['salary'].mean().round()
print('\nGrouped the dataframe by department and took mean of the salary:\n\n', group_dep_sal_mean)


#using multiple aggregations
group_dep_sal_hours = df.groupby('department')[['salary', 'workHours']].agg(['mean', 'max', 'min'])
print('\nGrouped the dataframe by department for salary, workHours and took mean, max and min:\n\n', group_dep_sal_hours)


#using multiple aggregation with named labels but allows more functions to use
group_dep_sal_hours_named = (
    df.groupby('department')
      .agg(
          salary_mean=('salary', lambda x: round(x.mean(), 2)),
          salary_max=('salary', 'max'),
          salary_min=('salary', 'min'),
          workHours_mean=('workHours', lambda x: round(x.mean(), 2)),
          workHours_max=('workHours', 'max'),
          workHours_min=('workHours', 'min')
      )
)
print('\nGrouped the dataframe by department for salary, workHours and took mean and rounded it, max and min with named labels:\n\n', group_dep_sal_hours_named)



'''
------------------------------------------------
Filtering Groups
------------------------------------------------
    df.groupby('City').filter(lambda x: x['Salary'].mean() > 50000)

'''
