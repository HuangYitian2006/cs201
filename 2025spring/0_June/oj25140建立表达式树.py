from collections import deque


class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def levelorder(root:Node):
    q=deque()
    q.append(root)
    ans=[]
    while q:
        x=q.popleft()
        if x.left: q.append(x.left)
        if x.right: q.append(x.right)
        ans.append(x.val)
    ans.reverse()
    return ''.join(ans)
for _ in range(int(input())):
    x=input()
    stk=[]
    for i in x:
        node = Node(i)
        if i.islower():
            stk.append(node)
        else:
            node.right=stk.pop()
            node.left=stk.pop()
            stk.append(node)
    root=node
    print(levelorder(root))
