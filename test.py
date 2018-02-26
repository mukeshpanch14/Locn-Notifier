import requests
url="https://www.amfiindia.com/spages/NAVAll.txt"
r=requests.get(url)
with open("out.txt",'wb') as f:
	f.write(r.content)


re=open("out.txt",'r')
for line in re.readlines():
	print(line)
	