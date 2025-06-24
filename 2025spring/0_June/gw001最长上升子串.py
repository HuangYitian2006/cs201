n=int(input())
for i in range(n):
    x=input()
    lth=len(x)
    a=[]
    for i in range(lth):
        a.append(int(x[i]))
    ans=1
    l,r,now,nowl=0,0,a[0],1
    while r<lth-1:
        r+=1
        if a[r]>=now:
            nowl+=1
            ans=max(nowl,ans)
        else:
            l=r
            nowl=1
            #print(r)
        now = a[r]
    print(ans)