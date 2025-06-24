class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def build_tree(p,m):
    if not p or not m:
        return None
    root=TreeNode(p[0])
    ind=m.index(p[0])
    root.left=build_tree(p[1:1+ind],m[:ind])
    root.right=build_tree(p[ind+1:],m[ind+1:])
    return root

def postorder(root:TreeNode):
    if not root:
        return ''
    res=postorder(root.left)+postorder(root.right)+root.val
    return res
while True:
    try:
        pre = input()
        mid = input()
        root=build_tree(pre,mid)
        print(postorder(root))

    except EOFError:
        break