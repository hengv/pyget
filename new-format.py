import json,time
f = open('/data/json-raw/11136a.txt','r')
while True:
    c = open('/data/json-raw/newformat_0519.csv','a')
    line = f.readline()
    if not line:
        break
    r=json.loads(line)
    de=time.ctime()
    d=time.strptime(de,"%a %b %d %H:%M:%S %Y")
    if r['errorCode']==0:
        name=""
        score=""
        scorestatus=""
        companyname=""
        diameter=""
        high=""
        weight=""
        layout=""
        year=""
        ischecked=""
        fake=""
        if r['data']['attr']:
            attrs=r['data']['attr']
            for attr in attrs:
                if attr.split("：")[0]=="年份":
                    year = attr.split("：")[1]
                if attr.split("：")[0]=="版式":
                    layout=attr.split("：")[1]
                if attr.split("：")[0]=="直径":
                    diameter=attr.split("：")[1]
                if attr.split("：")[0]=="厚度":
                    high=attr.split("：")[1]
                if attr.split("：")[0]=="重量":
                    weight=attr.split("：")[1]
        id=r['data']['ratingCode']
        if r['data']['coinName']:
            name=r['data']['coinName']
        if r['data']['goodsScoreStatus']:
            scorestatus=r['data']['goodsScoreStatus']
        if r['data']['companyShortName']:
            companyname=r['data']['companyShortName']
        if r['data']['goodsScore']:
            score=r['data']['goodsScore']
        getTime=time.strftime("%Y-%m-%d %H:%M:%S",d)
        if str(r['data']['ratingInstallType']):
            ischecked=str(r['data']['ratingInstallType'])
        if str(r['data']['recoverSign']):
            fake=str(r['data']['recoverSign'])
        getStr=id+','+name+','+layout+','+scorestatus+','+score+','+companyname+','+diameter+','+high+','+weight+','+getTime+','+year+','+ischecked+','+fake+'\n'
        c.write(getStr)
        print(getStr)
    c.close()
f.close()

