import urllib.request
from bs4 import BeautifulSoup
url="https://www.filmibeat.com/telugu/movies-by-year.html"
movies=urllib.request.urlopen(url)
released=movies.read().decode("utf-8")

html_movies=released
soup=BeautifulSoup(html_movies,'html.parser')
print(soup)
m1=[]

m3=[]

m4=[]

m5=[]

movie1=soup.find_all("div",{"class":"movie-name"})
for i in movie1:
    m1.append(i.text.split())
movie3=soup.find_all("div",{"class":"cast"})
for k in movie3:
    m3.append(k.text.split())
movie4=soup.find_all("div",{"class":"director"})
for l in movie4:
    m4.append(l.text.split())
movie5=soup.find_all("div",{"class":"Banner"})
for m in movie5:
    m5.append(m.text.split())
for n in range(len(m1)):
    ms1=""
    ms3=""
    ms4=""
    ms5=""
    for a in m1[n]:
        ms1+=a
    for b in m3[n]:
        ms3+=b
    for c in m4[n]:
        ms4+=c
    for d in m5[n]:
        ms5+=d
    print("movie-name:{}\n{}\ndirector:{}\n{}".format(ms1,ms3,ms4,ms5))

    print("\n")
