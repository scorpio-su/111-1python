count = int(input().replace('\n',''))
ans=count if count%10 ==0 else str(count)+'\n'
print(ans)