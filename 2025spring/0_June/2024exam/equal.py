import sys
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    parent[find(x)]=find(y)
n=int(input())
parent=dict()
x=[]
for i in range(n):
    x.append(input())
    if x[i][0] not in parent: parent[x[i][0]] = x[i][0]
    if x[i][3] not in parent: parent[x[i][3]] = x[i][3]
    if x[i][1]=='=':
        union(x[i][0],x[i][3])
for i in range(n):
    if x[i][1]=='!':
        if find(x[i][0])==find(x[i][3]):
            print('False')
            sys.exit()
    '''if x[0] in parent and x[3] in parent:
        if x[1] == '=':  # union
            if find(x[0])!=find(x[3]):
                
        if x[1] == '!':
            if find(x[0])==find(x[3]):
                print('False')
                sys.exit()
    else:
        if x[0] not in parent: parent[x[0]]=x[0]
        if x[3] not in parent: parent[x[3]]=x[3]
        if x[1]=='=': #union
            union(x[0],x[3])'''

print('True')