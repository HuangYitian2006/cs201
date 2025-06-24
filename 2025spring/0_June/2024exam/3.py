from collections import deque

n=int(input())
g=[[0]*n for _ in range(n)]
for i in range(n-1):
    x,y=map(int,input().split())
    g[x][y],g[y][x]=1,1
res=set(map(int,input().split()))
q=deque()
q.append(0)
ans=1
v=[0]*n
v[0]=1
while q:
    x=q.popleft()
    for i in range(n):
        if g[x][i]==1 and v[i]==0 and i not in res:
            q.append(i)
            v[i]=1
            ans+=1
print(ans)