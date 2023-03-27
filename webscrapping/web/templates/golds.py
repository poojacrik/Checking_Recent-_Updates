import urllib.request
from bs4 import BeautifulSoup
url="https://gadgets360.com/finance/gold-rate-in-india"
price=urllib.request.urlopen(url)
gold=price.read().decode("utf-8")
html_doc = gold
soup = BeautifulSoup(html_doc, 'html.parser')
import re
g1=[]
s1=""
gold2=soup.find_all('table',{"id":"city_wise_data"})
for i in gold2:
    g1.append(i.text.split())
for j in g1:
    content=j[11:]

for l in content:
    s1+=l
city=re.findall('[a-zA-Z]+',s1)

g1=[]
g2=[]
g3=[]
gold2=soup.find_all("td", {"class":"_lft"})
for j in gold2:
    g1.append(j.text.split())
g1=g1[53:]

for i in range(0,len(g1),2):
    g2.append(g1[i])
for j in range(1,len(g1),2):
    g3.append(g1[j])
for z in range(len(g2)):
    s2=""
    s3=""
    s4=""
    for m in city[z]:
        s2+=m
    for n in g2[z]:
        s3+=n
        s3+=" "
    for o in g3[z]:
        s4+=o
        s4+=" "
    print("{}        {}          {}".format(s2,s3,s4))