import math
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def buildtree(num):
    root=TreeNode(num[0])
    for i in range(1,len(num)):
        node=root
        x=num[i]
        while True:
            if x<node.val:
                if node.left:
                    node=node.left
                else:
                    node.left=TreeNode(x)
                    break
            elif x>node.val:
                if node.right:
                    node=node.right
                else:
                    node.right=TreeNode(x)
                    break
            else: break
    return root

def levelorder(root):
    q=deque([root])
    ans=[]
    while q:
        x=q.popleft()
        ans.append(x.val)
        if x.left: q.append(x.left)
        if x.right: q.append(x.right)
    return ans

a=list(map(int,input().split()))
root=buildtree(a)
print(*levelorder(root))
