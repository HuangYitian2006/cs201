n=int(input())
stk=[]
now,ans=1,0
for _ in range(n*2):
    x=list(input().split())
    if x[0]=='add':
        stk.append(int(x[1]))
    elif x[0]=='remove':
        if stk:
            if stk[-1]==now:
                stk.pop()
            else:
                ans+=1
                stk.clear()
        now+=1
print(ans)