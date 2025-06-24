from collections import defaultdict
def check(lst):
    stk=[-1]
    now=0
    v=[0]*(n+1)
    while stk:
        if now==n: return 'YES'
        flag=1
        while flag:
            for i in g[stk[-1]]:
                if v[i]==0: flag=0 #有子节点没访问过
            if flag==1:
                v[stk.pop()]=1 #当前节点子节点全部访问过了，或者是没有子节点
        #print(stk,'!')
        for i in g[stk[-1]]:
            if i==lst[now] and v[i]==0:
                stk.append(i)
                v[i]=1
                now+=1
                #print(stk)
                break
        else: return 'NO'
    return 'NO'

n,m=map(int,input().split())
g=defaultdict(list)
for i in range(m):
    x,y=map(int,input().split())
    g[x].append(y)
    g[y].append(x)
for i in range(n):
    g[-1].append(i)
for _ in range(int(input())):
    lst=list(map(int,input().split()))
    print(check(lst))