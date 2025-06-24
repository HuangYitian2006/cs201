def find(x):
    if parent[x]!=x:return find(parent[x])
    else: return x

def union(x,y):
    parent[find(x)]=find(y)
num=0
while True:
    num+=1
    n,m=map(int,input().split())
    if n==m==0:break
    parent=[i for i in range(n+1)]
    for i in range(m):
        x,y=map(int,input().split())
        union(x,y)
    cnt=0
    for i in range(1,n+1):
        if parent[i]==i:
            cnt+=1
    print(f'Case {num}: {cnt}')