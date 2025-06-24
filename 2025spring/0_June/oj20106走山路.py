import heapq
dx=[0,1,0,-1]
dy=[1,0,-1,0]
m,n,p=map(int,input().split())
graph=[]
for _ in range(m):
    graph.append(list(input().split()))

def dijkstra(x1,y1,x2,y2):
    dist=[[float('inf')]*n for i in range(m)]
    if graph[x1][y1]=='#'or graph[x2][y2]=='#':
        return 'NO'
    h=[(0,x1,y1)]
    while h:
        lth,x,y=heapq.heappop(h)
        if (x,y)==(x2,y2):
            return lth
        if lth>dist[x][y]:continue
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny]!='#':
                if lth+abs(int(graph[nx][ny])-int(graph[x][y]))<dist[nx][ny]:
                    dist[nx][ny]=lth+abs(int(graph[nx][ny])-int(graph[x][y]))
                    heapq.heappush(h,(dist[nx][ny],nx,ny))
    return 'NO'



for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    print(dijkstra(x1,y1,x2,y2))