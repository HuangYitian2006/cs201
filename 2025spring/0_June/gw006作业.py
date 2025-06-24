def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    parent[find(x)]=find(y)
n,m=map(int,input().split())
parent=[i for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    union(x,y)
cnt=0
for i in range(1,n+1):
    if parent[i]==i: cnt+=1
print(cnt)