import pandas as pd
from DataSets import df

'''
Aggregation Methods: functions that summarize multiple values
                     into a single representative value.

------------------------------------------------
Basic Aggregation Methods (with Examples)
------------------------------------------------

1) sum(): returns the total of values

    Example 1 (Series):
        s.sum()

    Example 2 (DataFrame column):
        df['Marks'].sum()

------------------------------------------------

2) mean(): returns the average value

    Example 1 (Series):
        s.mean()

    Example 2 (Grouped Data):
        df.groupby('City')['Marks'].mean()

------------------------------------------------

3) max(): returns the maximum value

    Example 1 (Series):
        s.max()

    Example 2 (DataFrame column):
        df['Age'].max()

------------------------------------------------

4) min(): returns the minimum value

    Example 1 (Series):
        s.min()

    Example 2 (Grouped Data):
        df.groupby('Department')['Salary'].min()

------------------------------------------------

5) count(): returns number of non-missing values

    Example 1 (Series):
        s.count()

    Example 2 (DataFrame column):
        df['Marks'].count()

------------------------------------------------

6) median(): returns the middle value

    Example 1 (Series):
        s.median()

    Example 2 (DataFrame column):
        df['Age'].median()

------------------------------------------------

7) std(): returns standard deviation

    Example 1 (Series):
        s.std()

    Example 2 (Grouped Data):
        df.groupby('City')['Salary'].std()

------------------------------------------------

8) var(): returns variance

    Example 1 (Series):
        s.var()

    Example 2 (DataFrame column):
        df['Marks'].var()

------------------------------------------------
Important Aggregation Methods Used in Machine Learning
------------------------------------------------

Most frequently used during:
• Feature engineering
• EDA
• Model input preparation

------------------------------------------------
ML-Focused Aggregations
------------------------------------------------
    .mean()     → feature averaging
    .median()   → robust central tendency
    .sum()      → cumulative features
    .count()    → frequency features
    .std()      → feature dispersion
    .min()      → range features
    .max()      → range features
    .unique()   → give unique elements 
    .quantile() → percentile-based features
    .nunique()  → categorical richness

------------------------------------------------
ML Examples
------------------------------------------------
    Feature scaling insight:
        df[['Age', 'Salary']].mean()

    Group-based feature:
        df.groupby('City')['Salary'].mean()

    Outlier detection:
        df['Marks'].std()

------------------------------------------------
Important Notes
------------------------------------------------
    - Ignore NaN values by default
    - Often used with groupby()
    - Produce scalar or reduced output
    - Core part of ML feature engineering pipelines
'''

df1 = df

print(df1.columns)
print('\n\nData Frame:\n', df1)
print('\n\nMinimum age:\n', df1['Age'].min())
print('\n\nMaximum age:\n', df1['Age'].max())
print('\n\nMedian of the age:\n', df1['Age'].median())
print('\n\nAverage marks:\n', df1['Marks'].mean().astype(int))
print('\n\nTotal marks obtained:\n', df1['Marks'].sum())
print('\n\nStandart deviation between the ages:\n', df1['Age'].std())
print('\n\nQuantile of the marks:\n', df1['Marks'].quantile())
print(df['Name'].unique())

