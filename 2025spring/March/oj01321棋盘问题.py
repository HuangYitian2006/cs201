s,k=0,0
def dfs(row,num):
    global s,k
    if num==k:
        s+=1
        return
    if num+n-row<k or row>=n:
        return
    for i in range(n):
        if v[i]==0 and b[row][i]=='#':
            v[i]=1
            dfs(row+1,num+1)
            v[i]=0
    dfs(row+1,num)
while True:
    n,k=map(int,input().split())
    if n==k==-1:
        break
    b=[]
    for i in range(n):
        b.append(input())
    v,s=[0]*n,0
    dfs(0,0)
    print(s)