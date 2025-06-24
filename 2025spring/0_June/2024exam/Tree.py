class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dfs(node,l):
    if node.left==node.right is None:
        l.append(node.val)
        print(*l)
    if node.right:
        dfs(node.right,l+[node.val])
    if node.left:
        dfs(node.left,l+[node.val])

def check1(node):
    if node.left==node.right is None:
        return True
    l,r=1,1
    if node.left:
        l=check1(node.left) and node.val>node.left.val
    if node.right:
        r=check1(node.right) and node.val>node.right.val
    return l and r

def check2(node):
    if node.left==node.right is None:
        return True
    l,r=1,1
    if node.left:
        l=check2(node.left) and node.val<node.left.val
    if node.right:
        r=check2(node.right) and node.val<node.right.val
    return l and r
n = int(input())
a = list(map(int, input().split()))
node = []
for i in range(n):
    node.append(Node(a[i]))
for i in range(n):
    if 0 <= 2 * i + 1 < n: node[i].left = node[2 * i + 1]
    if 0 <= 2 * i + 2 < n: node[i].right = node[2 * i + 2]
dfs(node[0],[])
if a[0]>a[1]:
    if check1(node[0]): print('Max Heap')
    else: print('Not Heap')
else:
    if check2(node[0]): print('Min Heap')
    else: print('Not Heap')
