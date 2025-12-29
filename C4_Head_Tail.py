import pandas as pd

'''
head(n): head returns the first n rows of the DataFrame or Series
         Default value of n is 5. If n not give returns 5 rows from top.

tail(n): tail returns the last n rows of the DataFrame or Series
         Default value of n is 5. If n not give returns 5 rows from bottom.

'''


json_df = pd.read_json(r"D:\Codes\Python\Pandas\house_pricing.json")

print(f'\nHead: \n\n{json_df.head(10)}')
print(f'\nTail: \n\n{json_df.tail()}')