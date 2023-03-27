from django.shortcuts import render

from django.http import HttpResponse

def web(request):
    return render(request,"web-scraping.html",{})
def movie(request):
    return render(request,"movies.html",{})
def cricket(request):
    return render(request,"cricket_score.html",{})
def job(request):
    return render(request,"jobs.html",{})
def gold(request):
    return render(request,"index.html",{})

def gol(request):
    import urllib.request
    from bs4 import BeautifulSoup
    url="https://gadgets360.com/finance/gold-rate-in-india"
    price=urllib.request.urlopen(url)
    gold=price.read().decode("utf-8")
    html_doc = gold
    soup = BeautifulSoup(html_doc, 'html.parser')
    import re
    goldlist1=[]
    goldlist2=[]
    goldlist3=[]
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
        goldlist1.append(s2)
        goldlist2.append(s3)
        goldlist3.append(s4)
    return render(request, "index.html",{'l1':goldlist1,'l2':goldlist2,'l3':goldlist3})
def crick(request):
    import urllib.request
    from bs4 import BeautifulSoup
    url="https://www.mykhel.com/cricket/live-scores/"
    live=urllib.request.urlopen(url)
    data=live.read().decode("utf-8")
    html_doc = data
    soup = BeautifulSoup(html_doc, 'html.parser')
    crik1=[]
    crik2=[]
    crik3=[]
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
        #print("{}\n{}\n{}\n".format(str1,str2,str3))
        crik1.append(str1)
        crik2.append(str2)
        crik3.append(str3)
    return render(request,"cricket_Score.html",{"c1":crik1,"c2":crik2,"c3":crik3})
def mov(request):
    import urllib.request
    from bs4 import BeautifulSoup
    url="https://www.filmibeat.com/telugu/movies-by-year.html"
    movies=urllib.request.urlopen(url)
    released=movies.read().decode("utf-8")

    html_movies=released
    soup=BeautifulSoup(html_movies,'html.parser')
    mov1=[]
    mov2=[]
    mov3=[]
    mov4=[]
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
        #print("movie-name:{}\ncast:{}\ndirector:{}\n{}".format(ms1,ms3,ms4,ms5))
        mov1.append(ms1)
        mov2.append(ms3)
        mov3.append(ms4)
        mov4.append(ms5)
    return render(request,"movies.html",{"movi1":mov1,"movi2":mov2,"movi3":mov3,"movi4":mov4})
def jobnoti(request):
    import urllib.request
    from bs4 import BeautifulSoup
    url="https://www.freshersworld.com/computer-science-engineering-cse-jobs/2222149"
    jobs=urllib.request.urlopen(url)
    new=jobs.read().decode("utf-8")

    html_jobs=new
    soup=BeautifulSoup(html_jobs,'html.parser')
    job1=[]
    job2=[]
    job3=[]
    job4=[]
    job5=[]
    job6=[]
    job7=[]
    job8=[]
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
        #print("{}.company-name:{}\n\nRole:{}\n\nQualification:{}\n\nJob-Description:{}\n\nLocation:{}\n\n{}\n\nExperience:{}\n\n".format(a,s1,s2,s3,s4,s5,s6,s7))
        job1.append(a)
        job2.append(s1)
        job3.append(s2)
        job4.append(s3)
        job5.append(s4)
        job6.append(s5)
        job7.append(s6)
        job8.append(s7)
    return render(request,"jobs.html",{"jo1":job1,"jo2":job2,"jo3":job3,"jo4":job4,"jo5":job5,"jo6":job6,"jo7":job7,"jo8":job8})
