import urllib.request
from bs4 import BeautifulSoup
url="https://www.mykhel.com/cricket/live-scores/"
live=urllib.request.urlopen(url)
data=live.read().decode("utf-8")
html_doc = data
soup = BeautifulSoup(html_doc, 'html.parser')
l1=[]
l2=[]
l3=[]
score1=soup.find_all("div",{"class":"os-match-desc-left"}) 
for i in score1:
    l1.append(i.text.split())
score2=soup.find_all("div",{"class":"os-match-desc-right"})
for j in score2:
    l2.append(j.text.split())
score3=soup.find_all("div",{"class":"os-match-summary"})
for k in score3:
    l3.append(k.text.split())

for a in range(len(l3)):
    str1=" "
    str2=" "
    str3=" "
    for m in l1[a]:
        str1+=m
        str1+" "
    for n in l2[a]:
        str2+=n
        str2+" "
    for o in l3[a]:
        str3+=o
        str3+" "
    print("{}\n{}\n{}\n".format(str1,str2,str3))
    print("\n\n")


