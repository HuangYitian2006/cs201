import heapq
from collections import defaultdict


def dijkstra(s, t):
    distance = {point: float('inf') for point in points}
    path = {point: '' for point in points}
    distance[s] = 0
    path[s] = s
    h = [(0, s)]
    heapq.heapify(h)
    while h:
        d, now = heapq.heappop(h)
        if d > distance[now]: continue  # 表示最短距离已经更新过了，这条路没有用了
        if now == t: break  # 到目标的路径已经为最短路，可不再做后续处理
        for v, w in maps[now]:
            nd = d + w
            if nd < distance[v]:
                distance[v] = nd
                path[v] = path[now] + f'->({w})->{v}'
                heapq.heappush(h, (nd, v))
    return path[t]


p = int(input())
points = []
maps = defaultdict(list)
for i in range(p):
    points.append(input())
q = int(input())
for i in range(q):
    x, y, d = input().split()
    d = int(d)
    maps[x].append((y, d))
    maps[y].append((x, d))
for _ in range(int(input())):
    s, t = input().split()
    print(dijkstra(s, t))
