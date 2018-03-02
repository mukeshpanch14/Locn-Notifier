import pandas as pd
import datetime
import SendMsg as SM

data=pd.read_csv('output.csv')

data.set_index("SCODE",inplace=True)
data.head()

scheme_code=119598
scheme_name=data.loc[scheme_code][2]
curr_nav=data.loc[scheme_code][3]

today=datetime.datetime.now()
today=today.strftime("%d/%m/%y")
print(today)
print(scheme_name)
print(curr_nav)

msg=today+" "+scheme_name+" "+"Current Nav- "+curr_nav
print(msg)

se=SM.SendMsg(msg,"+918280041455")
se.SendMessage()

