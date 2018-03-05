import pandas as pd
import datetime


class CheckNav(object):
	def __init__(self,scode):
		self.scode=scode

	def getMsg(self):

		today=datetime.datetime.now()
		today=today.strftime("%d%m%y")
		csv_filename="NAV_"+today+".csv"

		data=pd.read_csv(csv_filename)

		data.set_index("SCODE",inplace=True)
		data.head()

		
		scheme_name=data.loc[self.scode][2]
		curr_nav=data.loc[self.scode][3]
			
		msg=scheme_name+" "+"Current Nav- "+curr_nav
		return msg