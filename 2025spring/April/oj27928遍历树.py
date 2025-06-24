class TreeNode:
    def __init__(self,val,deg):
        self.val=val
        self.deg=deg
        self.children=[]
        self.isroot=True

def traversal(nd:TreeNode):
    num=[nd.val]
    res=[]
    for i in nd.children:
        num.append(i.val)
    num.sort()
    for i in num:
        if i==nd.val:
            res+=[i]
        else:
            res+=traversal(node[i])
    return res

n=int(input())
node=dict()
s=[]
for i in range(n):
    s.append(list(map(int,input().split())))
    node[s[i][0]]=TreeNode(s[i][0],len(s[i])-1)
for i in range(n):
    for j in range(len(s[i])-1):
        node[s[i][0]].children.append(node[s[i][j+1]])
        node[s[i][j+1]].isroot=False
root=0
for i in node.values():
    if i.isroot:
        root=i
print(*traversal(root),sep='\n')