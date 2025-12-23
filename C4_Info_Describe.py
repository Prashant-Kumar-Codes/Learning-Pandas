import pandas as pd


'''
info(): provides a concise summary of the DataFrame structure.
        It is mainly used to understand data types, missing values, and memory usage.

    Syntax: df.info()

    Parameters:
        verbose         (bool, optional)          - show full informatio 
        memory_usage    (bool or 'deep', optional)- show memory consumptio  
        show_counts     (bool, optional)          - show non-null counts
    (Most of the time, it is used without parameters.) 

    What it Shows:
        Number of rows and columns
        Column names
        Data type of each column
        Non-null (non-missing) values count
        Memory usage
'''
'''
describe(): generates statistical summary of numerical data in the DataFrame.
            It is mainly used for data analysis and understanding distribution  .

    Syntax:   df.describe()
   

    Parameters:
        include  - specify data types to include ( 'number' ,  'object' ,  'all' )
        exclude  - specify data types to exclude
        percentiles  - list of percentiles to calculate

    What it Shows (Numeric Columns):
        count 
        mean 
        std  (standard deviation - how much other values deviates w.r.t the median)
        min 
        25% ,  50%  (median),  75% 
        max 


    Example:
        df.describe()
        df.describe(include='all')
        
'''
'''
    Difference Between  info()  and  describe()   

| Feature              |  info()            |  describe()         |
| -------------------- | ------------------ | ------------------- |
| Purpose              | Structure overview | Statistical summary |
| Output type          | Text summary       | Tabular statistics  |
| Shows data type      | Yes                | No                  |
| Shows missing values | Yes                | Partially (count)   |
| Shows memory usage   | Yes                | No                  |
| Used in              | Data inspection    | Data analysis       |
| Applies to           | All columns        | Mostly numeric      |


'''

dataFrame = pd.read_json("house_pricing.json")
# dataFrameInfo = dataFrame.info()

data = {
    'Name': ['Ram', 'Shyam', 'Gyan'],
    'Age': [10, 20, 30],
    'City': ['Mohali', 'Jaipur', 'Delhi']
}

dataFrame2 = pd.DataFrame(data)

print('\n\nData Frame 2\n\n', dataFrame2)
print('\n\nData Frame 2 - info \n\n', dataFrame2.info())
print('\n\nData Frame 2 - describe \n\n', dataFrame2.describe())


print('\n\nData Frame - info\n\n', dataFrame.info())
print('\n\nData Frame - describe\n\n', dataFrame.describe())

