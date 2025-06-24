while True:
    try:
        a=input()
        stk=[]
        ans=[' ']*len(a)
        for i in range(len(a)):
            if a[i]=='(':
                stk.append(i)
            if a[i]==')':
                if stk: stk.pop()
                else: ans[i]='?'
        while stk:
            ans[stk.pop()]='$'
        print(a)
        print(''.join(ans))

    except EOFError:
        break