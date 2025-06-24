n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(m):
    x=input().split()
    if x[0]=='C':
        for i in range(n):
            a[i]+=int(x[1])
            a[i]%=65536
    if x[0]=='Q':
        s=0
        for i in range(n):
            b=bin(a[i])[2:][::-1]
            if int(x[1])<len(b) and b[int(x[1])]=='1':
                s+=1
        print(s)

