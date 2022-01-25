from requests import get
from argparse import ArgumentParser
from bs4 import BeautifulSoup
from random import choice
from colorama import Fore,init
import json

def not_completed(hint:str):
  print(Fore.YELLOW+f"Sorry, this function({hint}) is not completed.")
  exit(1)

def get_problems(d:int,types:str)->list:
  param={"type":types,"difficulty":d}
  header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
  page=1
  res=[]
  while True:
    param["page"]=page
    r=get("https://www.luogu.com.cn/problem/list",params=param,headers=header)
    r.raise_for_status()
    soup=BeautifulSoup(r.content,"lxml")
    try:
      prob_cont=soup.body.div.div.ul
    except:
      break
    prob_list=prob_cont.find_all("a")
    if len(prob_list)==0:
      break
    for prob in prob_list:
      res.append(str(prob["href"]))
    page+=1
  return res

default_sources=["P","B","CF","AT","UVA","SP"]

def main():
  init(autoreset=True)
  parser=ArgumentParser()
  group=parser.add_mutually_exclusive_group()
  group.add_argument("-s","--source",help="specify problem sources({}), use commas to separate".format(", ".join(default_sources)),dest="src")
  group.add_argument("-mc","--monthly-contest",help="choose problems from luogu monthly contests",action="store_true",dest="mc")
  parser.add_argument("difficulties",help="specify problem difficulties(1~7), use commas to separate")
  args=parser.parse_args()
  tp=0
  src=args.src
  if args.mc:
    tp=1
    not_completed("-mc, --monthly-contest")
  elif src!=None:
    src=src.split(",")
    lst=list(set(src))
    valid=set(default_sources)
    for elem in lst:
      if elem not in valid:
        print(Fore.RED+f"error: problem sources cannot be recognized({elem})")
        exit(1)
  else:
    src=default_sources
  if tp==0:
    prob_set=json.load(open("./problems.json"))
    try:
      diffs=list(map(int,args.difficulties.split(",")))
    except:
      print(Fore.RED+"error: problem difficulties cannot be recognized")
      exit(1)
    else:
      for x in diffs:
        if x<0 or x>7:
          print(Fore.RED+"error: problem difficulties cannot be recognized")
          exit(1)
    probs={}
    for i in set(diffs):
      print(f"Fetching problems with difficulty {i}")
      for s in src:
        qry=f"{i},{s}"
        if qry not in prob_set:
          prob_set[qry]=get_problems(i,s)
        if i not in probs:
          probs[i]=[]
        probs[i]+=prob_set[qry]
    for i in diffs:
      ch=choice(probs[i])
      probs[i].remove(ch)
      print(ch)
    json.dump(prob_set,open("./problems.json","w"))

if __name__=="__main__":
  main()
