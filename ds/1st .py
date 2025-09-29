import pandas as pd


d= {'col1': [1,2,3,4,5], 'col2': [4,5,7,8,9], 'col3': [7,8,9,1,5]}

df = pd.DataFrame(data=d)
Total_Column= df.shape[1]

Total_Row= df.shape[0] 

print(df)
print("\n\nNumber of Column = ",Total_Column)
print("Number of Row = ",Total_Row)