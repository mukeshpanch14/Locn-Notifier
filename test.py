import requests
import csv


url="https://www.amfiindia.com/spages/NAVAll.txt"
r=requests.get(url)
with open("out.txt",'wb') as f:
	f.write(r.content)


re=open("out.txt",'r')

wr=open("output.csv",'a')
for line in re.readlines():
	if len(line)>0 and line[0]>='0' and line[0]<='9':
		items=line.split(";")
		writer=csv.writer(wr)
		writer.writerows(items)
	"""if len(line)>0 and line[0] >= '0' and line[0] <= '9':
     #items=line.split(";")"""
     	
