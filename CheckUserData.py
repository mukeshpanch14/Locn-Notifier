import pandas as pd
import CheckNav as CN
import datetime

user_df=pd.read_csv("userdata.csv")

for row in user_df.itertuples():
	mobile_no=str(row[3])
	scode=row[2]
	scodes=scode.split(',')
	msg=""
	for s in scodes:
		sin=int(s)
		cn=CN.CheckNav(sin)
		msg=msg+"\n"+cn.getMsg()
	today=datetime.datetime.now()
	today=today.strftime("%d/%m/%y")
	final_msg=today+msg
	print(final_msg)

	


	