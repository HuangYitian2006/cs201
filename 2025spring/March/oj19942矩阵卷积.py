m,n,p,q=map(int,input().split())
a,t=[],[]
for i in range(m):
    a.append(list(map(int,input().split())))
for i in range(p):
    t.append(list(map(int,input().split())))
ans=[[0]*(n-q+1) for i in range(m-p+1)]
for i in range(m-p+1):
    for j in range(n-q+1):
        for k in range(p):
            for l in range(q):
                ans[i][j]+=a[i+k][j+l]*t[k][l]
for i in range(m-p+1):
    print(*ans[i])
