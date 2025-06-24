from collections import defaultdict, deque


def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    parent[find(x)]=find(y)
flag=0
def dfs(x):
    global flag
    if flag==1: return
    for i in graph[x]:
        if v[i]==1 and not flag:
            if i!=p[x]:
                print('loop:yes')
                flag=1
                return
        else:
            v[i]=1
            p[i]=x
            dfs(i)
            p[i]=-1
n,m=map(int,input().split())
parent=[x for x in range(n)]
xg=[[0]*n for i in range(n)]
graph=defaultdict(list)
for i in range(m):
    x,y=map(int,input().split())
    xg[x][y],xg[y][x]=1,1
    graph[x].append(y)
    graph[y].append(x)
    union(x,y)
cnt=0
for i in range(n):
    if find(i)==i: cnt+=1
if cnt>1:print('connected:no')
else: print('connected:yes')
v=[0]*n
p=[-1]*n
flag=0
v[0]=1
dfs(0)
if flag==0:print('loop:no')

