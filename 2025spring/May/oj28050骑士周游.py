flag=0
dx=[-2,-2,-1,-1,1,1,2,2]
dy=[1,-1,2,-2,2,-2,1,-1]
def dfs(x,y,step):
    global flag
    if flag:return
    if step==n**2:
        flag=1
    for i in range(8):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and v[nx][ny]==0:
            v[nx][ny]=1
            dfs(nx,ny,step+1)
            v[nx][ny]=0


n=int(input())
sx,sy=map(int,input().split())
v=[[0]*n for i in range(n)]
v[sx][sy]=1
dfs(sx,sy,1)
if flag: print('success')
else: print('fail')

