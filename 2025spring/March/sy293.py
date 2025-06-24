stk=[]
for i in range(int(input())):
    x=input().split()
    if x[0]=='pop':
        if stk:
            print(stk.pop())
        else:print(-1)
    else:
        stk.append(int(x[1]))