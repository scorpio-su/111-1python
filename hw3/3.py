def convertMillis(mills):
    time1=mills//1000
    return str(time1//3600)+':'+str(time1//60)+':'+str(time1%60)

num=list(map(int, input().replace('\n','').split(' ')))

for i in num:
    print(convertMillis(i))
