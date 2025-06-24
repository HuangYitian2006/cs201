import heapq
n = int(input())
graph = [[] for i in range(n)]
for i in range(n - 1):
    x = list(input().split())
    for j in range(int(x[1])):
        graph[ord(x[0]) - 65].append((ord(x[2 + j * 2]) - 65, int(x[2 + j * 2 + 1])))  # ord('A')==65
        graph[ord(x[2 + j * 2]) - 65].append((ord(x[0]) - 65, int(x[2 + j * 2 + 1])))
#print(graph)
ans=0
h=[(0,0)]
v=[0]*n
while h:
    lth,star=heapq.heappop(h)
    if v[star]==0:
        ans+=lth
        v[star]=1
        for x in graph[star]:
            heapq.heappush(h,(x[1],x[0]))
print(ans)
