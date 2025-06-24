from collections import deque

n,m=map(int,input().split())
a=list(map(int,input().split()))
q=deque()
for i in range(n):
    q.append((i+1,a[i]))
while len(q)>1:
    x=q.popleft()
    if x[1]>m: q.append((x[0],x[1]-m))
print(q[0][0])