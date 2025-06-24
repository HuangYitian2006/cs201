from collections import deque

m,n=map(int,input().split())
a=list(map(int,input().split()))
q=deque()
ans=0
for i in a:
    if i not in q:
        ans+=1
        q.append(i)
    if len(q)>m: q.popleft()
print(ans)