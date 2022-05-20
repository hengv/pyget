import csv

f=open("/data/json-raw/coins.csv",'r')
lines = csv.DictReader(f)
# next(lines)
for line in lines:
    
    
    if line['size']:
        s = line['size'].split(',')
        if s[0]:
            if len(s)==2:
                if s[1][-1]=='g':
                    weight=s[1][:-1]
                else:
                    weight=s[1]
            else:
                weight=''
            shape=s[0].split('*')
            if shape[0]:
                diameter=shape[0]
            if len(shape)==2:
                if shape[1][-2:]=='mm':
                    high=shape[1][:-2]
                else:
                    high=shape[1]
            else:
                high=''
    else:
        weight=''
        diameter=''
        high=''
    if line['score']:
        scoreStatus=line['score'][0]
        scorenumber=line['score'][1:]
    newline = line['id']+','+line['name']+','+line['layout']+','+scoreStatus+','+scorenumber+','+','+diameter+','+high+','+weight+','+line['getTime']+','+line['year']+','+line['isChecked']+','+line['fake']
    if weight != '' and high != '' and diameter != "":
        cfile = open("/data/json-raw/used/newformat-old-0519.csv",'a')
        cfile.write(newline+'\n')
        cfile.close()
    else:
        nfile = open("/data/json-raw/used/newformat-old-0519.csv",'a')
        nfile.write(newline+'\n')
        nfile.close()
    print(newline,'\n')
f.close()