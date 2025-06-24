from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]
def bfs(sx,sy):
    v=[[0]*(c+2) for i in range(r+2)]
    q=deque([(sx,sy,0)])
    v[sx][sy]=1
    while q:
        x,y,step=q.popleft()
        if g[x][y]=='E':
            return step
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if g[nx][ny]!='#' and v[nx][ny]==0:
                q.append((nx,ny,step+1))
                v[nx][ny]=1
    return 'oop!'
for _ in range(int(input())):
    r,c=map(int,input().split())
    g=[['.']*(c+2) for i in range(r+2)]
    for i in range(r+2):
        for j in range(c+2):
            if i==0 or i==r+1 or j==0 or j==c+1:
                g[i][j]='#'
    for i in range(r):
        g[i+1][1:c+1]=input()
    for i in range(r+2):
        for j in range(c+2):
            if g[i][j]=='S':
                print(bfs(i,j))
