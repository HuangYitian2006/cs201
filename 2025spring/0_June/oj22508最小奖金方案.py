from collections import defaultdict, deque

n,m=map(int,input().split())
ans=[]
g=defaultdict(list)
inn=[0]*n
outt=[0]*n
for i in range(m):
    x,y=map(int,input().split())
    g[y].append(x)
    inn[x]+=1
    outt[y]+=1
q=deque()
for i in range(n):
    if inn[i]==0:
        q.append(i)
s,k=0,0
while q:
    l=len(q)
    s+=(100+k)*l
    for _ in range(l):
        now=q.popleft()
        for x in g[now]:
            inn[x]-=1
            if inn[x]==0:
                q.append(x)
    k+=1
print(s)
