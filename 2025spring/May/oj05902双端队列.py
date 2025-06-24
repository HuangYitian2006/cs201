from collections import deque

for _ in range(int(input())):
    q=deque()
    for _ in range(int(input())):
        s,x=map(int,input().split())
        if s==1:
            q.append(x)
        if s==2:
            if x==0:
                q.popleft()
            if x==1:
                q.pop()
    if q:print(*q)
    else: print('NULL')
