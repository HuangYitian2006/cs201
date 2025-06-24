import heapq
from collections import defaultdict

n,m=map(int,input().split())
g=defaultdict(list)
for i in range(m):
    x,y,z=map(int,input().split())
    g[x].append((y,z))
dist=[float('inf')]*(n+1)
h=[(0,1)]
while h:
        d,x=heapq.heappop(h)
        if d>dist[x]:continue
        for y,z in g[x]:
            if d+z<dist[y]:
                dist[y]=d+z
                heapq.heappush(h,(dist[y],y))
print(dist[n])