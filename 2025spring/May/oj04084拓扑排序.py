from collections import deque
v,a=map(int,input().split())
inn=[0]*(v+1)
outt={i:[] for i in range(v+1)}
for i in range(a):
    x,y=map(int,input().split())
    outt[x].append(y)
    inn[y]+=1
vis=[0]*(v+1)
cnt=0
ans=[]
while cnt<v:
    for i in range(1,v+1):
        if inn[i]==0 and vis[i]==0:
            ans.append('v'+str(i))
            vis[i]=1
            for j in outt[i]:
                inn[j]-=1
            break
    cnt+=1
print(*ans)