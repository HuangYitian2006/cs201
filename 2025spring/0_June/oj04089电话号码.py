class TrieNode:
    def __init__(self):
        self.child={}
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, nums):
        curnode = self.root
        for x in nums:
            if x not in curnode.child:
                curnode.child[x] = TrieNode()
            curnode=curnode.child[x]

    def search(self, num):
        curnode = self.root
        for x in num:
            if x not in curnode.child:
                return 0
            curnode = curnode.child[x]
        return 1

for _ in range(int(input())):
    a=[]
    for _ in range(int(input())):
        a.append(input())
    a.sort(reverse=True)
    t=Trie()
    cnt=0
    for x in a:
        cnt+=t.search(x)
        t.insert(x)
    print('NO'if cnt else 'YES')

