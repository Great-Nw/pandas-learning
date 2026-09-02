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

# #  PYTHON SERIES  
# # A series is like a list except it keeps track of the positions of each item in it.
# #Creating a Series and adding Labels to it
# print("===PYTHON SERIES===")
# daily_interest = pd.Series([120,110,100,105],
# ['Monday','Tuesday','Wednesday','Thursday'])
# print(daily_interest['Thursday'])
# #We can also create from dictionary
# skills = pd.Series({
#     'Python':'Advanced',
#     'JavaScript':'Intermediate',
#     'Rust':'Beginner'
# })
# #Using index labels
# ex1 = pd.Series(['Jan','Feb','Mar'],
#                 index=['1','2','3'])
# print(ex1['1'])

# #Using Position
# print(ex1.iloc[0])

# #Multiple elements
# print(ex1[['1','2']])

# #Series Operation: Operating with series
# streak = pd.Series([10,20,8,17],
# index=['Mon','Tue','Wed','Thu'])

# issues = pd.Series([2,4,1,6],
# index=['Mon','Tue','Wed','Thu'])

# #Calculate streak to issues ratio
# ratio = streak / issues
# print(ratio)

# print(f"Total issues opened: {issues.sum()}")
# print(f"Best day: {streak.max()}")
# print(f"Average:{streak.mean():.1f}")

# #We can even filter
# busy_days = streak[streak > 10]
# print(busy_days)

# #Series Methods
# grades = pd.Series([44,60,89,60],
# index=['Alice','Greg','Joey','Paulie'])

# print(grades.mean())
# print(grades.max())
# print(grades.min())
# print(grades.value_counts())
# #Get quick statistical summary of Series
# print(grades.describe())

# #Series Attributes
# contrib = pd.Series(
#     [20,30,12,45,0,9,7],
#     index=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
# )

# print(f"Values:{contrib.values}, Series:{contrib.index}")
# print("Size:",contrib.size)
# print("Data Type:",contrib.dtype)
# print("Index Data type:",contrib.index.dtype)
# #Check if data is complete
# print(f"Any Missing Days? {contrib.hasnans}")

# #Practice Problem 2
# #Bug Tracker Analysis
# #We are given bugs and we must:
# #1.Count high-priority bugs (priority >= 4)
# #2.Calculatte average bug priority
# #3.Sort bugs by priority(descending)
# #4.Find unique priority levels

# print("===PRACTICE PROBLEM 2===")
# bugs = pd.Series({
#     'login-error': 5,
#     'slow-loading': 3,
#     'broken-link': 2,
#     'typo': 1,
#     'crash': 5,
#     'security': 5,
#     'ui-glitch': 2
# })
# #1.
# high_priority = bugs[bugs >= 4]
# print(high_priority.value_counts())

# #2.
# mean_priority = bugs.mean()
# print(mean_priority)

# #3.
# descend_priority = bugs.sort_values(ascending=False)
# print(descend_priority)

# #4.
# unique_priors = bugs.unique()
# print(unique_priors)

# #DATAFRAME BASICS
# #A dataframe is a 2d dimensional array unlike series
# new_data = {
#  'name': ['Ally','Bob','Charles'],
#  #first column
#  'age': [11,12,17],
#  #second column
#  'city': ['NY','SF','LA']
# }
# newDf = pd.DataFrame(new_data)
# print(newDf)

# new_data = [{'name':'Ally','age':11, 'city':'NY'},
#             {'name':'Bob','age':12, 'city':'SF'},
#             {'name':'Charles','age':17,'city':'LA'}]
# print(pd.DataFrame(new_data))
# #Attributes of DataFrames
# #.shape
# print(newDf.shape)
# #.columns
# print(newDf.columns)
# #..index
# print(newDf.index)
# #Get data from city column, also applies to other column
# print(newDf['city'])
# #Add Gender Column
# newDf['gender'] = 'F','M','M'
# print(newDf)
# #print data from multiple columns
# print(newDf[['name','gender','age']])
# #Accessing rows
# #Let's access the first row
# first = newDf.loc[0]
# print(first)
# #View first/last rows
# print(newDf.head(2))
# print(newDf.tail(1))
# #Add a new row
# newDf.loc[3] = {'name':'David','age':20,'city':'LA','gender':'M'}
# print(newDf)

# #PROGRAM EXERCISE 3
# #Analyze popular python packages to understand what makes them succesful!
# #We must:
# #1.Examine the dataframe structure
# #2.Sort project by popularity
# #3.Find Projects with large communities
# #4.Calculate stars per contribution ratio
# libraries = {
#     'name': ['numpy', 'pandas', 'requests', 'flask', 'django'],
#     'stars': [22000, 35000, 48000, 58000, 65000],
#     'contributors': [1200, 2800, 950, 3500, 2300],
#     'language': ['Python', 'Python', 'Python', 'Python', 'Python'],
#     'first_release': ['2006', '2009', '2011', '2010', '2005']
# }
# #1.
# libDf = pd.DataFrame(libraries)
# print(libDf.info())
# #2.
# print(libDf.sort_values(ascending=False,by='stars'))
# #3.
# print(libDf.loc[libDf['contributors'] > 2000])
# #4.
# libDf['stars_per_contributor'] = libDf['stars'] / libDf['contributors']
# print(libDf)

#DATAFRAME OPERATIONS
#Filtering dataframes
#Dataframe filtering helps you to find all entries in the dataframe meeting all certain criteria
# workers = pd.DataFrame({
#     'name':['Alice','Kevin','Chris'],
#     'jobs':['SE','MLE','CE'],
#     'years_joined':[2016,2022,2025],
#     'income':[2e5,1.2e5,1e5]
# })
#Getting recent workers
# recent = f"New workers are :{workers[workers['years_joined'] > 2024]}"
# print(recent)
# #we can use it more specifically
# print(workers[workers['name'] == 'Alice']) and (workers[workers['years_joined'] == 2016])
# #Sorting Dataframes using .sort_values()
# byYears = workers.sort_values(by='years_joined',ascending=False)
# print(byYears)
# #sort by multiple values
# byYearsandIncome = workers.sort_values(by=['years_joined','income'],ascending=[False,False])
# print(byYearsandIncome)
# #Handling missing data
import numpy as np

# exFrame = pd.DataFrame({
#     'username': ['pythonista', 'js_lover', 'rust_fan'],
#     'last_login': ['2024-01-01', None, '2024-01-03'],
#     'points': [100, np.nan, 150]
# })

# # Find where the gaps are
# print(exFrame.isna().sum())
# #We can clean it up or we can fill it ourselves using .fillna()
# cleaned_exFrame = exFrame.dropna()
# print(cleaned_exFrame)
# filled_exFrame = exFrame.fillna(0)
# print(filled_exFrame)
# #.apply() is used to use functions on rows in the dataframe
# filled_exFrame['username'] = filled_exFrame['username'].apply(str.upper)
# print(filled_exFrame)
# #We can apply functiosn we make
# def rank(points):
#     if points >= 150:
#         return 'Expert'
#     elif points >= 100:
#         return 'Intermediate'
#     return 'Beginner'
# filled_exFrame['rank'] = filled_exFrame['points'].apply(rank)
# print(filled_exFrame)
#Apply works on both Series and Dataframes
#===PROBLEM EXERCISE 5===
# Welcome to code review analytics!

# Code review data
data2 = {
    'pr_id': range(1, 11),
    'author': ['alice', 'bob', 'alice', 'charlie', 'bob',
              'david', 'charlie', 'alice', 'bob', 'david'],
    'files_changed': [5, 10, 3, 8, 4, 
                     7, 6, 9, 2, 5],
    'additions': [100, 200, 50, 300, 75,
                 150, 250, 180, 40, 90],
    'deletions': [80, 150, 30, 200, 50,
                 100, 200, 120, 20, 60],
    'review_time': [2.5, 4.0, 1.0, 3.5, 2.0,
                   2.8, 3.2, 3.8, 1.5, 2.2],
    'status': ['merged', 'merged', 'merged', 'rejected', 'merged',
              'pending', 'merged', 'rejected', 'merged', 'pending']
}

df = pd.DataFrame(data2)

# 1. Calculate net changes (additions - deletions) per PR
df['net_changes'] = df['additions'] - df['deletions']
print(df)

# 2. Find PRs with high impact (files > 5 or net_changes > 100)
high_impact =  df[(df['files_changed'] > 5) | (df['net_changes'] > 100)]
print(high_impact)

# 3. Get average review time per author
review_times = df.groupby('author').agg({'review_time': 'mean'})
print(review_times)

# 4. Create a status summary (count of merged/rejected/pending per author)
status_summary = df.pivot_table(
    index='author',
    columns='status',
    aggfunc='size',
    fill_value=0
)
print(status_summary)