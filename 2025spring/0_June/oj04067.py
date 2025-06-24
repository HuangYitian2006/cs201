while True:
    try:
        x=input()
        a=[]
        for i in range(len(x)):
            a.append(x[i])
        b=a.copy()
        b.reverse()
        if a==b:print('YES')
        else:print('NO')
    except EOFError:break