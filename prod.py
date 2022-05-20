import requests,time,json
from requests_toolbelt.adapters import source

ips = ['10.0.0.4','10.0.0.5','10.0.0.6','10.0.0.7','10.0.0.8','10.0.0.9',
       '10.0.0.10','10.0.0.11','10.0.0.12','10.0.0.13','10.0.0.14','10.0.0.15','10.0.0.16','10.0.0.17','10.0.0.18','10.0.0.19',
       '10.0.0.20','10.0.0.21','10.0.0.22','10.0.0.23','10.0.0.24','10.0.0.25','10.0.0.26','10.0.0.27','10.0.0.28','10.0.0.29',
       '10.0.0.80','10.0.0.81','10.0.0.82','10.0.0.83','10.0.0.84','10.0.0.85','10.0.0.86','10.0.0.87','10.0.0.88','10.0.0.89',
       '10.0.0.90','10.0.0.91','10.0.0.92','10.0.0.93','10.0.0.94','10.0.0.95','10.0.0.96','10.0.0.97','10.0.0.98','10.0.0.99',
       '10.0.0.100','10.0.0.101','10.0.0.102','10.0.0.103']
headers = {
    'Referer': 'https://www.gongbocoins.com/',
    'Content-Length': '27',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': 'wapi.gongbocoins.com'
}


url = 'https://wapi.gongbocoins.com/gbca/orderCoin/getWebsiteRatingInfo'
c = open("/data/config.txt",'r')
nums = c.read()
numb = int(nums)+1
c.close()
n=1
m=0
s = requests.Session()
while True:
    if m==50:
        m=0
    new_source = source.SourceAddressAdapter(ips[m])
    s.mount('http://', new_source)
    s.mount('https://', new_source)
    nums = str(numb)
    body = {
        "ratingCode": nums
    }
    r=s.post(url=url,headers=headers, json=body)
    f = open("/data/a.txt",'a')
    l = open("/data/log.txt",'a')
    e = open("/data/error.txt",'a')
    c = open("/data/config.txt",'w')
    txt=json.dumps(r.json(),ensure_ascii=False)+'\n'
    if r.json()['errorCode'] == 0:
        logtxt=time.ctime()+' '+ips[m]+' '+nums+' S'+'\n'
        f.write(txt)
        f.close()
    elif r.json()['errorCode'] == 3016:
        logtxt=time.ctime()+' '+ips[m]+' '+nums+' no number Failure'+'\n'
        e.write(txt)
        e.close()
    else:
        logtxt=time.ctime()+' '+ips[m]+' '+nums+' reject Failure'+'\n'
        e.write(txt)
        e.close()
        time.sleep(10)
    l.write(logtxt)
    l.close()
    c.write(nums)
    c.close()
    numb=numb+1
    m=m+1
    time.sleep(1)
    if numb == 1114200000:
        break
