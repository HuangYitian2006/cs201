while True:
    try:
        x=input()
        stk=[]
        ans=[' ']*len(x)
        for i in range(len(x)):
            if x[i]=='(':
                stk.append(i)
            elif x[i]==')':
                if stk: stk.pop()
                else: ans[i]='?'
        for i in stk:
            ans[i]='$'
        print(x)
        print(''.join(ans))
    except EOFError:break