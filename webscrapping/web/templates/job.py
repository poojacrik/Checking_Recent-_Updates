import urllib.request
from bs4 import BeautifulSoup
url="https://www.freshersworld.com/computer-science-engineering-cse-jobs/2222149"
jobs=urllib.request.urlopen(url)
new=jobs.read().decode("utf-8")
html_jobs=new
soup=BeautifulSoup(html_jobs,'html.parser')
print(soup)
j1=[]
j2=[]
j3=[]
j4=[]
j5=[]
j6=[]
j7=[]
update2=soup.find_all("h3",{"class":"latest-jobs-title font-16 margin-none inline-block"})
for i in update2:
    j1.append(i.text.split())
update3=soup.find_all("div",{"class":"col-md-12 col-xs-12 col-lg-12 padding-none left_move_up_new"})
for j in update3:
    j2.append(j.div.text.split())
update4=soup.find_all("div",{"class":"qualification-block"})
for k in update4:
    j3.append(k.text.split())
update5=soup.find_all("span",{"class":"desc"})
for l in update5:
    j4.append(l.text.split())
update6=soup.find_all("div",{"class":"col-md-5 col-xs-5 col-lg-5 padding-none"})
for m in update6:
    j5.append(m.text.split())
update7=soup.find_all("div",{"class":"col-md-4 col-xs-4 col-lg-4 padding-none"})
for n in update7:
    j6.append(n.text.split())
j6=j6[2:]
update8=soup.find_all("span",{"class":"experience"})
for o in update8:
    j7.append(o.text.split())
for a in range(len(j1)):
    s1=""
    s2=""
    s3=""
    s4=""
    s5=""
    s6=""
    s7=""
    for b in j1[a]:
        s1+=b
    for c in j2[a]:
        s2+=c
    for d in j3[a]:
        s3+=d
    for e in j4[a]:
        s4+=e
    for f in j5[a]:
        s5+=f
    for g in j6[a]:
        s6+=g
    for h in j7[a]:
        s7+=h
    print("{}.company-name:{}\n\nRole:{}\n\nQualification:{}\n\nJob-Description:{}\n\nLocation:{}\n\n{}\n\nExperience:{}\n\n".format(a,s1,s2,s3,s4,s5,s6,s7))

