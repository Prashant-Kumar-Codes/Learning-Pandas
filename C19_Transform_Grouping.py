import pandas as pd

'''
transform(): applies a function to each group and returns an output
             with the SAME shape as the original DataFrame or Series.
             It is mainly used for feature engineering and normalization.

------------------------------------------------
Syntax
------------------------------------------------
    df.groupby(key).transform(func)
    df['new_col'] = df.groupby(key)[col].transform(func)

------------------------------------------------
Parameters
------------------------------------------------
    key   - column(s) used for grouping
    col   - column on which transformation is applied
    func  - function (mean, sum, lambda, custom logic)

------------------------------------------------
What it Does
------------------------------------------------
    - Applies a function per group
    - Returns aligned values (same length as original data)
    - Does NOT reduce rows (unlike agg())
    - Ideal for creating new features

------------------------------------------------
Why transform() exists
------------------------------------------------
    groupby().agg()   → reduces rows (summary)
    groupby().transform() → preserves rows (feature creation)

------------------------------------------------
Examples
------------------------------------------------

1) Salary normalized by department mean
    df['salary_norm'] = df.groupby('department')['salary'].transform(
        lambda x: x / x.mean()
    )

2) Replace missing values using group mean
    df['salary'] = df['salary'].fillna(
        df.groupby('department')['salary'].transform('mean')
    )

3) Z-score standardization (ML feature scaling)
    df['salary_z'] = df.groupby('department')['salary'].transform(
        lambda x: (x - x.mean()) / x.std()
    )

4) Difference from department average
    df['salary_diff'] = df['salary'] - df.groupby('department')['salary'].transform('mean')

------------------------------------------------
For Series
------------------------------------------------
    s.groupby(key).transform(func)

------------------------------------------------
Important Points
------------------------------------------------
    - Output size == input size
    - Works only with groupby()
    - Very common in ML preprocessing
    - Safe replacement for loops
    - No FutureWarning issues

------------------------------------------------
Common ML Use Cases
------------------------------------------------
    ✔ Feature normalization per category
    ✔ Missing value imputation
    ✔ Group-based scaling
    ✔ Relative metrics creation

------------------------------------------------
Comparison
------------------------------------------------
    agg()       → summarization
    transform() → feature engineering
    apply()     → flexible but slower

------------------------------------------------
Professional Tip
------------------------------------------------
    Use transform() whenever you want group logic
    WITHOUT losing original rows.

'''
'''
------------------------------------------------
ML-Oriented Examples
------------------------------------------------
    City-based feature:
        df['city_mean_salary'] =
        df.groupby('City')['Salary'].transform('mean')

    Frequency encoding:
        df['city_count'] =
        df.groupby('City')['City'].transform('count')

    Robust feature:
        df.groupby('Department')['Marks'].median()
'''