import requests
import csv


url="https://www.amfiindia.com/spages/NAVAll.txt"
r=requests.get(url)
with open("out.txt",'wb') as f:
	f.write(r.content)

filepath='out.txt'

with open(filepath) as fp:
    lines=fp.readlines()
    
lines = [x.strip() for x in lines] 

wr=open("output.csv",'w')
for line in lines:
    if len(line)>0 and line[0]>'0' and line[0]<'9':
        #print(line)
        items=line.split(';')
        print(items)
        writer=csv.writer(wr)
        writer.writerow(items)