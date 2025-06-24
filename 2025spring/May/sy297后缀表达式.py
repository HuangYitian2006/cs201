a=list(input().split())
stk=[]
ans=[]
priority={'+':0,'-':0,'*':1,'/':1}
for i in range(len(a)):
    if i%2==0:
        ans.append(a[i])
    if i%2==1:
        if not stk: stk.append(a[i])
        else:
            while stk and priority[a[i]]<=priority[stk[-1]]:
                ans.append(stk.pop())
            else:
                stk.append(a[i])
while stk:
    ans.append(stk.pop())
print(*ans)



# 3 + 4 * 5 - 9
# 3 4 5 * + 9 -