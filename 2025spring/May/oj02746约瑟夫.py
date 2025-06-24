from collections import deque

while True:
    n,m=map(int,input().split())
    if n==m==0: break
    a=deque(list(range(1,n+1)))
    while len(a)>1:
        for i in range(m-1):
            a.append(a.popleft())
        a.popleft()
    print(a[0])
