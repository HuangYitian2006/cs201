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
    nums=[]
    for _ in range(int(input())):
        nums.append(input())
    nums.sort(reverse=True)
    trie=Trie()
    s=0
    for i in nums:
        s+=trie.search(i)
        trie.insert(i)
    if s: print('NO')
    else: print('YES')