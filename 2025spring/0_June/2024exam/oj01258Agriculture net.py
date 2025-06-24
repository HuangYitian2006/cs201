import heapq
from collections import deque, defaultdict

while True:
    try:
        n=int(input())
        g=defaultdict(list)
        for i in range(n):
            x=list(map(int,input().split()))
            for j in range(n):
                if j!=i:
                    g[i].append((x[j],j)) #(距离，农场)

        ans=0
        v=[0]*n
        h=[(0,0)]
        while h:
            lth,farm=heapq.heappop(h)
            if v[farm]==0:
                ans+=lth
                v[farm]=1
                for i in g[farm]:
                    if v[i[1]]==0:heapq.heappush(h,i)
        print(ans)

    except EOFError:break