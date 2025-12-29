from DataSets import df
import numpy as np

print(df.columns)
print('\n\n', df.Name, '\n\n')
print('\n\n', df['Name'], '\n\n')
print('\n\n', df['Name'].values, '\n\n')
print('\n\n', df[['Name']], '\n\n')
print('\n\n', df[['Name']].values, '\n\n')
print('\n\n', np.array(df[['Name']]), '\n\n')