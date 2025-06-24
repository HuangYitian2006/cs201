from collections import deque

n,k=map(int,input().split())
q=deque()
for i in range(n):
    q.append(i+1)
ans=[]
while len(q)>1:
    for i in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())
print(*ans)