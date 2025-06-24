n=int(input())
ind=[set(map(int,input().split()[1:])) for i in range(n)]
for _ in range(int(input())):
    s=list(map(int,input().split()))
    i=0
    while s[i]!=1:i+=1
    ans=ind[i].copy()
    for j in range(0,i):
        if s[j]==-1: ans-=ind[j]
    for j in range(i+1,n):
        if s[j]==-1: ans-=ind[j]
        elif s[j]==1: ans&=ind[j]
    if ans:print(*sorted(list(ans)))
    else:print('NOT FOUND')