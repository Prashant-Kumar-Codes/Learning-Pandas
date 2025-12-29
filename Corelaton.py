import pandas as pd
from DataSets import df, empdf

print(df.columns)
# print(df.corr()) ----> This is causing error
print(df.corr(numeric_only=True))
print(empdf.corr(numeric_only=True, method='kendall'))
