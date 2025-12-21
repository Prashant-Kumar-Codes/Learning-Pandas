import pandas as pd

# A Series is a one-dimensional labeled array in Pandas.
#Syntax: pd.Series(list of elements, index=list of labels)
pdSeries = pd.Series([10,20,30,40])
print(pdSeries,type(pdSeries))

pdSeries1 = pd.Series([10,20,30,40], index=['ten','twenty','thirty','fourty'])
print(pdSeries1, type(pdSeries1))

try:
    print(pdSeries == pdSeries1)
except:
    print('Cannot be compared')

# Important Attributes
    # s.index
    # s.values
    # s.dtype
    # s.shape
    # s.size

print(f'index: {pdSeries.index}\tvalues: {pdSeries.values}, {type(pdSeries.values)}\tdtype: {pdSeries.dtype}\tshape: {pdSeries.shape}\tsize: {pdSeries.size}')


# dataframe
dict1 = {
    'column1_numbers': [1,2,3,4,5,6,7,8,9,10],
    'column2_alphabet':['a','b','c'],
    'column3_empty':[]
}

max_len = max(len(value) for value in dict1.values())

# print(max_len)

for key in dict1:
    for i in range(max_len - len(dict1[key])):
        if len(dict1[key]) < 10:
            dict1[key].append('NaN')
            
# print(dict1)
dict1_DataFrame = pd.DataFrame(dict1)
print(dict1_DataFrame)

dict1_DataFrame.to_csv('check1.csv', index=0)

print(len(dict1_DataFrame), type(dict1_DataFrame))

from datetime import datetime, timedelta
OTP_EXPIRY = 60
RESEND_INTERVAL = 60
STALE_ACCOUNT_SECONDS = 3600

cutoff = datetime.now() - timedelta(seconds=STALE_ACCOUNT_SECONDS)

print(cutoff)
print(STALE_ACCOUNT_SECONDS)

x ='Prashant'
print(x[0:3])
