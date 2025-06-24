class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def preorder(root:Node):
    if root is None: return ''
    ans=root.val+preorder(root.left)+preorder(root.right)
    return ans

def buildtree(m,p):
    if len(m)==0: return None
    root=Node(p[-1])
    x=m.index(p[-1])  #找到根的位置，左树长也为x
    root.left=buildtree(m[:x],p[:x])
    root.right=buildtree(m[x+1:],p[x:-1])
    return root

mid=input()
post=input()
root=buildtree(mid,post)
print(preorder(root))