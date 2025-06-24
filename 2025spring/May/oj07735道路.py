import heapq
k=int(input()) #maxcost
n=int(input()) #citynum
r=int(input()) #roadnum
road={i:[] for i in range(1,n+1)}
for i in range(r):
    s,d,l,t=map(int,input().split())
    road[s].append((d,l,t))
dis=[[float('inf')]*(k+1) for i in range(n+1)]
h=[(0,1,0)]
flag=0
while h:
    cdis,ccity,ccost=heapq.heappop(h)
    if cdis>dis[ccity][ccost]:
        continue
    if ccity==n:
        print(cdis)
        flag=1
        break
    for d,l,t in road[ccity]:
        if ccost+t<=k and cdis+l<dis[d][ccost+t]:
            dis[d][ccost + t]=cdis+l
            heapq.heappush(h,(cdis+l,d,ccost+t))
if flag==0: print(-1)