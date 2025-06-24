def dfs(x):
    global flag
    if flag:return
    for i in range(n):
        if (x,i) in a:
            if v[i]!=0:
                flag=1
                return
            else:
                v[i]=1
                dfs(i)
                v[i]=0
n,m=map(int,input().split())
a=set()
for i in range(m):
    x,y=map(int,input().split())
    a.add((x,y))
v=[0]*n
flag=0
for i in range(n):
    if flag:break
    if v[i]==0:
        dfs(i)
if flag: print('Yes')
else: print('No')