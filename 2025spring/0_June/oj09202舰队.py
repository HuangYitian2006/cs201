from collections import defaultdict, deque

for _ in range(int(input())):
    n,m=map(int,input().split())
    graph=defaultdict(list)
    inn=defaultdict(int)
    outt=defaultdict(int)
    for i in range(m):
        x,y=map(int,input().split())
        graph[x].append(y)
        inn[y]+=1
        outt[x]+=1
    q=deque()
    for i in range(1,n+1):
        if inn[i]==0:
            q.append(i)
    ans=deque()
    while q:
        now=q.popleft()
        ans.append(now)
        for i in graph[now]:
            inn[i]-=1
            if inn[i]==0:
                q.append(i)
    if len(ans)==n: print('No')
    else:print('Yes')



