import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL='https://www.google.com/search?q=australia+vs+england&oq=aus&aqs=chrome.0.69i59j69i57j0l4.6722j0j7&sourceid=chrome&ie=UTF-8#sie=m;/g/11ghtdpt67;5;/m/021vk;dt;fp;1;;'
headers={"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
truns=0
fours=0
sixes=0
wic=""
ove=""

def chkscore():
 global truns
 global fours
 global sixes
 global wic
 global ove

 page=requests.get(URL,headers=headers)
 soup=BeautifulSoup(page.content,'lxml')


 score=soup.findAll("div", class_="imspo_mh_cricket__score-major")[1].get_text()
 overs=soup.findAll("div", class_="imspo_mh_cricket__score-minor")[1].get_text()
 runs=""
 c=0
 wickets=""
 for i in score :
    if(i!="/" and c==0):
        runs=runs+i
        
    if(i=="/"):
        c=1
    if(c==1):
        wickets=wickets+i
 runs=float(runs)
 wickets=(wickets[1:2])
 overs=(overs[1:4])

 if(runs>truns):
     if(runs-truns==4):
         four=four+1
         print("FOUR")
     if(runs-truns==6):
         sixes=sixes+1
         print("SIX")
 if(wic!=wickets):
     print("OUT")
     wic=wickets
 if(overs!=ove):
  ove=overs
  truns=runs
  print("NEW BALL"+"\n")
  print("Runs")
  print(runs)
  
   
  print("Loss"+"\n"+wickets+"\n"+"overs"+"\n"+overs)
  return(overs)


 
overs=""
while(overs!="50" or wic!="10"):

  overs=chkscore()
print("number of sixes")
print(sixes)
print("number of sixes")
print(fours)


  
 




