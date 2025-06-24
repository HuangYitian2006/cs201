from collections import deque


class Node:
    def __init__(self,ind,deg):
        self.index=ind
        self.degree=deg
        self.children=[]

def buildtree(s):
    ind=0
    root=Node(s[0],int(s[1]))
    ind+=2
    q=deque([root])
    while q:
        node=q.popleft()
        for i in range(node.degree):
            child=Node(s[ind],int(s[ind+1]))
            ind+=2
            node.children.append(child)
            q.append(child)
    return root

def postorder(node):
    ans=[]
    for i in range(node.degree):
        ans.extend(postorder(node.children[i]))
    ans.append(node.index)
    return ans
n=int(input())
ans=[]
for _ in range(n):
    s=input().split()
    root=buildtree(s)
    ans.extend(postorder(root))
print(*ans)


