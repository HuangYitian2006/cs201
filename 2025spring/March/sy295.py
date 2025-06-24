def dfs(ans,num,x):
    if num==n:
        anslist.append(ans.copy())
    if stk:
        ans.append(stk.pop())
        dfs(ans,num+1,x)
        stk.append(ans.pop())
    if x:
        stk.append(x.pop())
        dfs(ans,num,x)
        x.append(stk.pop())
n=int(input())
x=[n-i for i in range(n)]
anslist,stk=[],[]
used=[0]*n
dfs([],0,x)
for i in anslist:
    print(*i)
