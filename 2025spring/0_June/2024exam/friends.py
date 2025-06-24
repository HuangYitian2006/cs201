def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    x0,y0=find(x),find(y)
    if c[x0-1]<c[y0-1]:
        parent[y0]=x0
    else:
        parent[x0]=y0
n,m=map(int,input().split())
c=list(map(int,input().split()))
parent=[i for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    union(x,y)
ans=0
for i in range(1,n+1):
    if parent[i]==i:
        ans+=c[i-1]
print(ans)