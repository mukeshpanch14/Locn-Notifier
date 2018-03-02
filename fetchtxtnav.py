"""
Fetching data from the website of AMFI India in the format of .txt
Inputs-none
Output-.txt file--> NAV_ddmmyy.txt
"""


import requests
import datetime


today=datetime.datetime.now()
today=today.strftime("%d%m%y")
print(today)

txt_filename="NAV"+"_"+today+".txt"
print(txt_filename)



url="https://www.amfiindia.com/spages/NAVAll.txt"
r=requests.get(url)
with open(txt_filename,'wb') as f:
	f.write(r.content)

f.close()
