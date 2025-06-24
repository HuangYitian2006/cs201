class TreeNode:
    def __init__(self,val):
        self.val=val
        self.deg=0
        self.children=[]

ind=0
def addchildren(root):
    global ind
    deg=0
    while s[ind]!=')':
        ind+=1
        if s[ind].isalpha():
            stk.append(TreeNode(s[ind]))
            deg+=1
        if s[ind]=='(':
            addchildren(stk[-1])
    ind+=1
    root.deg=deg
    c=[]
    for i in range(deg):
        c.append(stk.pop())
    for i in range(deg):
        root.children.append(c.pop())

def preorder(node):
    if not node:
        return ''
    res=node.val
    for i in range(node.deg):
        res+=preorder(node.children[i])
    return res

def postorder(node):
    if not node:
        return ''
    res=''
    for i in range(node.deg):
        res+=postorder(node.children[i])
    res+=node.val
    return res

s=input()
root=TreeNode(s[0])
ind=1
stk=[root]
if len(s)>1:
    addchildren(root)
print(preorder(root))
print(postorder(root))


