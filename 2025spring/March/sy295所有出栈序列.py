def dfs(ans,num,x):
    if num==n:
        anslist.append(ans.copy())
    if stk:
        ans.append(stk.pop())
        dfs(ans,num+1)
        stk.append(ans.pop())
    for i in range():
        if used[i]==0:
            stk.append(x.pop())
            dfs(ans,num,x)
            stk.pop()
            used[i]=0
n=int(input())
x=[n-i for i in range(n)]
anslist,stk=[],[]
used=[0]*n
dfs([],0,x)
print(anslist)
