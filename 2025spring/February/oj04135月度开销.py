def check(mx):
    cnt,s=0,0
    for i in cost:
        s+=i
        if s>mx:
            cnt+=1
            s=i
    return cnt<m
n,m=map(int,input().split())
cost=[]
for i in range(n):
    cost.append(int(input()))
l,r=max(cost)-1,sum(cost)
while l+1<r:
    mid=(l+r)//2
    if check(mid):
        r=mid
    else:
        l=mid
print(r)