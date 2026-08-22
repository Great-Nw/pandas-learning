import pandas as pd

# data= {
#     'Name': ['Charles','Nick'],
#     'Age': [24,89] 
# }

# df = pd.DataFrame(data)

# print(df)
# #Quick preview of dataframe
# print(df.head(1))
# #Statistical Description of dataframe
# print(df.describe())
# #Getting extra info about dataframe
# print(df.info())
# #Getting data from a specific column 
# print(df[['Name']])
# print(df['Age'])

# #.shape, returns a tuple containing values for rows and columns
# print(df.shape)
# #.columns returns a list containing every column name in the dataframe
# print(df.columns)
# #.dtypes return tehe data types for data stored in each columns
# print(df.dtypes)

# #  PRACTICE PROBLEM
# # We are given a data to work with. We are to:
# # Turn the given data into a dataframe.
# # 1.Extract items under the 'price' column
# # 2.Use .info() to get the info of the product data
# # 3.Use .describe() to get statistical information

# #Product Data
# print("==PROGRAM EXERCISE.1==") #Indicating this as the first exercise given
# product_data = {
#     'name': ['Apple', 'Banana', 'Orange', 'Mango'],
#     'price': [0.5, 0.3, 0.6, 0.8],
#     'stock': [100, 120, 80, 60]
# }

# #Creating Dataframe of product data
# data_frame = pd.DataFrame(product_data)
# print(data_frame)

# #Extracting price column
# print(data_frame['price'])

# #Displaying extra information about Dataframe
# print(data_frame.info())

# #Getting Statistical information
# print(data_frame.describe())
# #indicating end of program exercise 1
# print("===PROGRAM EXERCISE 1 End.===")

#  PYTHON SERIES  
# A series is like a list except it keeps track of the positions of each item in it.
#Creating a Series and adding Labels to it
print("===PYTHON SERIES===")
daily_interest = pd.Series([120,110,100,105],
['Monday','Tuesday','Wednesday','Thursday'])
print(daily_interest['Thursday'])
#We can also create from dictionary
skills = pd.Series({
    'Python':'Advanced',
    'JavaScript':'Intermediate',
    'Rust':'Beginner'
})
#Using index labels
ex1 = pd.Series(['Jan','Feb','Mar'],
                index=['1','2','3'])
print(ex1['1'])

#Using Position
print(ex1.iloc[0])

#Multiple elements
print(ex1[['1','2']])

#Series Operation: Operating with series
streak = pd.Series([10,20,8,17],
index=['Mon','Tue','Wed','Thu'])

issues = pd.Series([2,4,1,6],
index=['Mon','Tue','Wed','Thu'])

#Calculate streak to issues ratio
ratio = streak / issues
print(ratio)

print(f"Total issues opened: {issues.sum()}")
print(f"Best day: {streak.max()}")
print(f"Average:{streak.mean():.1f}")

#We can even filter
busy_days = streak[streak > 10]
print(busy_days)

#Series Methods
grades = pd.Series([44,60,89,60],
index=['Alice','Greg','Joey','Paulie'])

print(grades.mean())
print(grades.max())
print(grades.min())
print(grades.value_counts())
#Get quick statistical summary of Series
print(grades.describe())

#Series Attributes
contrib = pd.Series(
    [20,30,12,45,0,9,7],
    index=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
)

print(f"Values:{contrib.values}, Series:{contrib.index}")
print("Size:",contrib.size)
print("Data Type:",contrib.dtype)
print("Index Data type:",contrib.index.dtype)
#Check if data is complete
print(f"Any Missing Days? {contrib.hasnans}")

#Practice Problem 2
#Bug Tracker Analysis
#We are given bugs and we must:
#1.Count high-priority bugs (priority >= 4)
#2.Calculatte average bug priority
#3.Sort bugs by priority(descending)
#4.Find unique priority levels

print("===PRACTICE PROBLEM 2===")
bugs = pd.Series({
    'login-error': 5,
    'slow-loading': 3,
    'broken-link': 2,
    'typo': 1,
    'crash': 5,
    'security': 5,
    'ui-glitch': 2
})
#1.
high_priority = bugs[bugs >= 4]
print(high_priority.value_counts())

#2.
mean_priority = bugs.mean()
print(mean_priority)

#3.
descend_priority = bugs.sort_values(ascending=False)
print(descend_priority)

#4.
unique_priors = bugs.unique()
print(unique_priors)