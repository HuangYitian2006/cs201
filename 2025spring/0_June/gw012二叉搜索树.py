class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def buildtree(post,mid):
    if len(post)==0: return None
    root=Node(post[0])
    ind=mid.index(post[0])
    root.left=buildtree(post[1:ind+1], mid[:ind])
    root.right=buildtree(post[ind+1:], mid[ind+1:])
    return root

def postorder(node):
    if not node:
        return ''
    return postorder(node.left)+postorder(node.right)+str(node.val)+' '
n=int(input())
post=list(map(int,input().split()))
mid=sorted(post)
root=buildtree(post,mid)
print(postorder(root))
