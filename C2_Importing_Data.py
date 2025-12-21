import pandas as pd

#reading data from CSV file into a dataframe
csv_df = pd.read_csv(r"D:\Codes\Python\Pandas\customers_1000.csv") # encoding = "utf-8" or "latin1"
# print(csv_df)

#reading data from JSON file into a dataframe
json_df = pd.read_json(r"D:\Codes\Python\Pandas\house_pricing.json")
# print(json_df)

#reading data from XLSX file into a dataframe
xlsx_df = pd.read_excel(r"D:\Codes\Python\Pandas\Project_dataset.xlsx")
#print(xlsx_df)

# to read the data from a cloud platform use "gcsfs" libraray




