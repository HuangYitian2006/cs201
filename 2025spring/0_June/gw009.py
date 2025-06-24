import math


class Node:
    def __init__(self,val):
        self.val=val
        self.children=[]
        self.degree=0
def cnt(node):
    s=0
    for x in node.children:
        if not leaf(x):
            s+=cnt(x)
    c=cntleaf(node)
    s+=math.ceil(c/2)
    return s

def cntleaf(node):
    s=0
    for x in node.children:
        if not x.children:
            s+=1
    return s
def leaf(node):
    if node.children:
        return False
    else: return True
n=int(input())
edge=[]
for i in range(n-1):
    x,y=map(int,input().split())
    if x>y: x,y=y,x
    edge.append((x,y))
edge.sort()
node=[0]
for i in range(1,n+1):
    node.append(Node(i))
root=node[1]
for b in edge:
    node[b[0]].children.append(node[b[1]])
    node[b[0]].degree+=1
print(cnt(root))
