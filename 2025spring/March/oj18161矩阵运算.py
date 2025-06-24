a,b,c=[],[],[]
ra,ca=map(int,input().split())
for i in range(ra):
    a.append(list(map(int,input().split())))
rb,cb=map(int,input().split())
for i in range(rb):
    b.append(list(map(int,input().split())))
rc,cc=map(int,input().split())
for i in range(rc):
    c.append(list(map(int,input().split())))
if ca==rb and ra==rc and cb==cc:
    ans=[[0]*cc for i in range(rc)]
    for i in range(rc):
        for j in range(cc):
            for k in range(ca):
                ans[i][j]+=a[i][k]*b[k][j]
            ans[i][j]+=c[i][j]
    for i in range(rc):
        print(*ans[i])
else: print('Error!')