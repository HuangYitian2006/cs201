n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
b=[]
for i in range(n):
    if b and b[-1][0]==a[i]:
        b[-1][1]+=1
    else: b.append([a[i],1])
#print(b)
now=0
for x in b:
    now+=x[1]
    if now==k:
        print(x[0])
        break
    elif (now>k and k!=0) or (k==0 and b[0][0]==1):
        print(-1)
        break
    elif k==0:
        print(1)
        break