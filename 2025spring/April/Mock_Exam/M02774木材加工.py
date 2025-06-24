n,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
l,r=0,max(a)
while l+1<r:
    m=(l+r)//2
    cnt=0
    for i in range(n):
        cnt+=a[i]//m
    if cnt>=k:
        l=m
    else:
        r=m
print(l)