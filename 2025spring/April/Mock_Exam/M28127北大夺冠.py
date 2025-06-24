from collections import defaultdict
m=int(input())
name=set()
ac=defaultdict(dict)
num=defaultdict(int)
submit=defaultdict(int)
for _ in range(m):
    s=list(input().split(','))
    if s[0] not in name:
        name.add(s[0])
    submit[s[0]]+=1
    if s[2]=='yes':
        if s[1] not in ac[s[0]]:
            num[s[0]]+=1
            ac[s[0]][s[1]]=1
name1=list(name)
name=[[x,num[x],submit[x]]for x in name1]
name.sort(key=lambda x:(-x[1],x[2],x[0]))
for i in range(min(12,len(name))):
    print(i+1,*name[i])
