n=int(input())
a=list(map(int,input().split()))
x=[n-i for i in range(n)]
stk=[x.pop()]
i=0
while i<n:
    if stk and stk[-1]==a[i]:
        stk.pop()
        i+=1
    elif x:
        stk.append(x.pop())
    else:
        print('No')
        break
else:
    print('Yes')
