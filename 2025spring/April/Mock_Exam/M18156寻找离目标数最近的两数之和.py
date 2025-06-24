t=int(input())
a=list(map(int,input().split()))
a.sort()
l,r=0,len(a)-1
d=float('inf')
ans=0
while l<r:
    s=a[l]+a[r]
    if abs(s-t)<d:
        ans=s
        d=abs(s-t)
    if abs(s - t) == d and ans > s:
        ans = s
    if s==t:
        break
    elif s<t:
        l+=1
    elif s>t:
        r-=1
print(ans)