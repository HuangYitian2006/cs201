from collections import defaultdict,deque

bucket=defaultdict(list)
n=int(input())
for _ in range(n):
    word=input()
    for i in range(4):
        bucket[word[:i]+'_'+word[i+1:]].append(word)
st,ed=input().split()
q=deque([st])
parent={st:st}#记录访问过的节点的上一个
flag=0
while q:
    now=q.popleft()
    if now==ed:
        flag=1
        break
    for i in range(4):
        for x in bucket[now[:i] + '_' + now[i + 1:]]:
            if x not in parent: #还没记录过就是还没visit
                parent[x]=now
                q.append(x)
if flag==1:
    ans=[ed]
    y=ed
    while parent[y]!=y:
        ans.append(parent[y])
        y=parent[y]
    ans.reverse()
    print(*ans)
else: print('NO')
