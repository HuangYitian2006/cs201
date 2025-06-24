while True:
    try:
        a=input()
        flag=1
        for i in range(len(a)):
            if a[i]!=a[len(a)-1-i]:
                flag=0
        print('YES' if flag else 'NO')
    except EOFError:
        break