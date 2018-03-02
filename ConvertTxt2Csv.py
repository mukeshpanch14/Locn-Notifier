"""
Conversion of txt file to csv file 
Inputs-filename(NAV_ddmmyy.txt)
Output-.txt file--> NAV_ddmmyy.csv
"""

import requests
import datetime
import csv

class ConvertTxt2Csv(object):
	def __init__(self,txt_filename):
		self.txt_filename=txt_filename

	def convert(self):
		with open(self.txt_filename) as fp:
			lines=fp.readlines()

		fp.close()
		lines = [x.strip() for x in lines]


		today=datetime.datetime.now()
		today=today.strftime("%d%m%y")

		csv_filename="NAV_"+today+".csv"

		wr=open(csv_filename,'w', newline='')
		writer=csv.writer(wr)
		header=['SCODE','ISINP','ISINR','SCHEME_NAME','NAV','RPS','SP','DATE']
		writer.writerow(header)
		for line in lines:
			if len(line)>0 and line[0]>'0' and line[0]<'9':
				items=line.split(';')
				writer.writerow(items)

		wr.close()


