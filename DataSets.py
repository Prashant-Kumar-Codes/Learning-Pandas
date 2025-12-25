import pandas as pd

data = {
    'Name': ['Aman', 'Rohit', 'Sahil', 'Kunal', 'Neha', 'Anjali', 'Priya', 'Simran','Arjun', 'Vikas', 'Pooja', 'Nikhil','Riya', 'Sandeep', 'Karan', 'Isha'],
    'Age': [ 18, 19, 20, 21, 17, 19, 20, 18, 21, 22, 19, 20, 18, 23, 21, 19],
    'City':  ['Delhi', 'Mumbai', 'Chandigarh', 'Mohali', 'Ludhiana', 'Jaipur', 'Pune', 'Bengaluru', 'Noida','Gurugram', 'Delhi', 'Mumbai', 'Chandigarh', 'Mohali', 'Ludhiana', 'Ropar'],
    'Marks': [8.4, 7.9, 8.6, 7.5, 9.1, 8.2, 8.8, 7.6, 8.9, 7.8, 8.3, 8.7, 7.4, 8.1, 8.5, 9.0]
    }

employee_data = {
    'id' : [i for i in range(101, 120)],
    
    'name' : ['Aman', 'Rohit', 'Sahil', 'Kunal', 'Neha', 'Anjali', 'Priya', 'Simran','Arjun', 'Vikas', 'Pooja', 'Nikhil','Riya', 'Sandeep', 'Karan', 'Isha', 'Ramesh', 'Suresh', 'Pankaj', 'Sahil'],
    
    'salary' : [35000, 42000, 58000, 61000, 47000, 53000, 69000, 76000, 48000, 55000, 62000, 71000, 39000, 46000, 84000, 90000, 67000, 52000, 60000, 74000 ],
    
    'department' : ['Software Development', 'Data Science', 'Artificial Intelligence', 'Machine Learning', 'Cloud Computing', 'Cyber Security', 'IT Support', 'Network Engineering', 'DevOps', 'Quality Assurance', 'Product Management', 'Business Analysis', 'UI/UX Design', 'Web Development', 'Mobile App Development', 'Database Administration', 'System Administration', 'IT Consulting', 'Technical Support', 'Enterprise Applications'],
    
    'workHours' : [7, 8, 9, 6, 10, 8, 7, 9, 8, 6, 10, 7, 9, 8, 6, 7, 10, 9, 8, 7]
}

df = pd.DataFrame(data)
empdf = pd.DataFrame(employee_data)
csvDf = pd.read_csv(r'customers_1000.csv')
excelDf = pd.read_excel(r'Project_dataset.xlsx')
jsonDF = pd.read_json(r'house_pricing.json')

