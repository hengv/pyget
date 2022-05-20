import json,time
f = open('/data/json-raw/used/1113a.txt','r')
while True:
    c = open('/data/json-raw/used/ratingInstallType_2_add.csv','a')
    line = f.readline()
    if not line:
        break
    r=json.loads(line)
    de=time.ctime()
    d=time.strptime(de,"%a %b %d %H:%M:%S %Y")
    if r['errorCode']==0:
        if r['data']['ratingInstallType']==2:
            if not(r['data']['boxDetails']):
                continue
            for i in range(len(r['data']['boxDetails'])):
                print(r['data']['ratingInstallType'],i)
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
                if r['data']['boxDetails'][i]['attr']:
                    attrs=r['data']['boxDetails'][i]['attr']
                    for attr in attrs:
                        # print(attr)
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
                id=r['data']['ratingCode']+str(i)
                # idx=r['data']['boxDetails'][i]['ratingCode']
                if r['data']['boxDetails'][i]['coinName']:
                    name=r['data']['boxDetails'][i]['coinName']
                if r['data']['boxDetails'][i]['goodsScoreStatus']:
                    scorestatus=r['data']['boxDetails'][i]['goodsScoreStatus']
                if r['data']['companyShortName']:
                    companyname=r['data']['companyShortName']
                if r['data']['boxDetails'][i]['goodsScore']:
                    score=r['data']['boxDetails'][i]['goodsScore']
                getTime=time.strftime("%Y-%m-%d %H:%M:%S",d)
                if str(r['data']['boxDetails'][i]['ratingResult']):
                    ischecked=str(r['data']['boxDetails'][i]['ratingResult'])
                if str(r['data']['boxDetails'][i]['recoverSign']):
                    fake=str(r['data']['boxDetails'][i]['recoverSign'])
                getStr=id+','+name+','+layout+','+scorestatus+','+score+','+companyname+','+diameter+','+high+','+weight+','+getTime+','+year+','+ischecked+','+fake+'\n'
                c.write(getStr)
                print(getStr)
    c.close()
f.close()

