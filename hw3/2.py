max1, max2 = -1, -1
for _ in range(int(input())):
    num=int(input())
    if max1<num:  max1, max2=num, max1
    if max2==-1 and max1 > num: max2 = num

if max2 == -1: print('highest:', max1,'second-highest: no')
else: print('highest:', max1,'second-highest:',max2)
