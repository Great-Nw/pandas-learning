import pandas as pd

data= {
    'Name': ['Charles','Nick'],
    'Age': [24,89] 
}

df = pd.DataFrame(data)

print(df)
#Quick preview of dataframe
print(df.head(1))
#Statistical Description of dataframe
print(df.describe())
#Getting extra info about dataframe
print(df.info())
#Getting data from a specific column 
print(df[['Name']])
print(df['Age'])

#.shape, returns a tuple containing values for rows and columns
print(df.shape)
#.columns returns a list containing every column name in the dataframe
print(df.columns)
#.dtypes return tehe data types for data stored in each columns
print(df.dtypes)

#  PRACTICE PROBLEM
# We are given a data to work with. We are to:
# Turn the given data into a dataframe.
# 1.Extract items under the 'price' column
# 2.Use .info() to get the info of the product data
# 3.Use .describe() to get statistical information

#Product Data
print("==PROGRAM EXERCISE.1==") #Indicating this as the first exercise given
product_data = {
    'name': ['Apple', 'Banana', 'Orange', 'Mango'],
    'price': [0.5, 0.3, 0.6, 0.8],
    'stock': [100, 120, 80, 60]
}

#Creating Dataframe of product data
data_frame = pd.DataFrame(product_data)
print(data_frame)

#Extracting price column
print(data_frame['price'])

#Displaying extra information about Dataframe
print(data_frame.info())

#Getting Statistical information
print(data_frame.describe())
#indicating end of program exercise 1
print("===PROGRAM EXERCISE 1 End.===")

#  PYTHON SERIES  
# A series is like a list except it keeps track of the positions of each item in it.
#Creating a Series and adding Labels to it
print("===PYTHON SERIES===")
daily_interest = pd.Series([120,110,100,105],
['Monday','Tuesday','Wednesday','Thursday'])
print(daily_interest['Thursday'])
#We can also create from dictionary
