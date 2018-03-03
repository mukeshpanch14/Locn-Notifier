import pandas as pd 

user_df=pd.read_csv("userdata.csv")

for row in user_df.itertuples():
	print(row[3])
	