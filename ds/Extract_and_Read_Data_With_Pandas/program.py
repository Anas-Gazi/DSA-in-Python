import pandas as pd

# Correct path to your CSV file, not the .py file
health_data = pd.read_csv(r"c:\Users\arana\OneDrive\Desktop\DSA\ds\Extract_and_Read_Data_With_Pandas\health_data.csv")

health_data.dropna(axis=0,inplace=True) #clean NaN value
print(health_data.head()) #head() is used to show only top 5 row
print(health_data.info()) #info() is used to show data type
pd.set_option('display.max_columns',None)
print(health_data.describe())