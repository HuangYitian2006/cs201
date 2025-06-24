from collections import deque

while True:
    n,p,m=map(int,input().split())
    if n==p==m==0:
        break
    q=deque()
    ans=[]
    for i in range(n):
        q.appendleft(i)
    for i in range(p-1):
        q.appendleft(q.pop())
    while q:
        for i in range(m-1):
            q.appendleft(q.pop())
        ans.append(q.pop()+1)
    print(*ans,sep=',')