## 一、python基础

表2-2 可应用于任意Python序列的运算

| **Operation Name** | **Operator** | **Explanation**                         |
| ------------------ | ------------ | --------------------------------------- |
| indexing           | [ ]          | Access an element of a sequence         |
| concatenation      | +            | Combine sequences together              |
| repetition         | *            | Concatenate a repeated number of times  |
| membership         | in           | Ask whether an item is in a sequence    |
| length             | len          | Ask the number of items in the sequence |
| slicing            | [ : ]        | Extract a part of a sequence            |

表2-3 Python列表提供的方法

| **Method Name** | **Use**                | **Explanation**                                     |
| --------------- | ---------------------- | --------------------------------------------------- |
| `append`        | `alist.append(item)`   | Adds a new item to the end of a list                |
| `insert`        | `alist.insert(i,item)` | Inserts an item at the ith position in a list       |
| `pop`           | `alist.pop()`          | Removes and returns the last item in a list         |
| `pop`           | `alist.pop(i)`         | Removes and returns the ith item in a list          |
| `sort`          | `alist.sort()`         | Modifies a list to be sorted                        |
| `reverse`       | `alist.reverse()`      | Modifies a list to be in reverse order              |
| `del`           | `del alist[i]`         | Deletes the item in the ith position                |
| `index`         | `alist.index(item)`    | Returns the index of the first occurrence of `item` |
| `count`         | `alist.count(item)`    | Returns the number of occurrences of `item`         |
| `remove`        | `alist.remove(item)`   | Removes the first occurrence of `item`              |

表2-4 Python字符串提供的方法

| **Method Name** | **Use**                | **Explanation**                                           |
| --------------- | ---------------------- | --------------------------------------------------------- |
| `center`        | `astring.center(w)`    | Returns a string centered in a field of size `w`          |
| `count`         | `astring.count(item)`  | Returns the number of occurrences of `item` in the string |
| `ljust`         | `astring.ljust(w)`     | Returns a string left-justified in a field of size `w`    |
| `lower`         | `astring.lower()`      | Returns a string in all lowercase                         |
| `rjust`         | `astring.rjust(w)`     | Returns a string right-justified in a field of size `w`   |
| `find`          | `astring.find(item)`   | Returns the index of the first occurrence of `item`       |
| `split`         | `astring.split(schar)` | Splits a string into substrings at `schar`                |

元组与列表非常相似。它们的区别在于，元组和字符串一样是不可修改的。元组通常写成由括号包含并且以逗号分隔的一系列值。与序列一样，元组允许之前描述的任一操作。

集合（set）是由零个或多个不可修改的Python数据对象组成的无序集合。集不允许重复元素，并且写成由花括号包含、以逗号分隔的一系列值。空集由set()来表示。集是异构的。

表2-5 Python集合支持的运算

| **Operation Name** | **Operator**       | **Explanation**                                              |
| ------------------ | ------------------ | ------------------------------------------------------------ |
| membership         | in                 | Set membership                                               |
| length             | len                | Returns the cardinality of the set                           |
| `|`                | `aset | otherset`  | Returns a new set with those elements in at least one of the two sets |
| `&`                | `aset & otherset`  | Returns a new set with only those elements common to both sets |
| `-`                | `aset - otherset`  | Returns a new set with all items from the first set not in second |
| `<=`               | `aset <= otherset` | Asks whether all elements of the first set are in the second |

表2-6 Python集合提供的方法

| **Method Name** | **Use**                       | **Explanation**                                              |
| --------------- | ----------------------------- | ------------------------------------------------------------ |
| `union`         | `aset.union(otherset)`        | Returns a new set with all elements from both sets           |
| `intersection`  | `aset.intersection(otherset)` | Returns a new set with only those elements common to both sets |
| `difference`    | `aset.difference(otherset)`   | Returns a new set with all items from first set not in second |
| `issubset`      | `aset.issubset(otherset)`     | Asks whether all elements of one set are in the other        |
| `add`           | `aset.add(item)`              | Adds item to the set                                         |
| `remove`        | `aset.remove(item)`           | Removes item from the set                                    |
| `pop`           | `aset.pop()`                  | Removes an arbitrary element from the set                    |
| `clear`         | `aset.clear()`                | Removes all elements from the set                            |

表2-7 Python字典支持的运算

| **Operator** | **Use**          | **Explanation**                                              |
| ------------ | ---------------- | ------------------------------------------------------------ |
| `[]`         | `myDict[k]`      | Returns the value associated with `k`, otherwise its an error |
| `in`         | `key in adict`   | Returns `True` if key is in the dictionary, `False` otherwise |
| `del`        | del `adict[key]` | Removes the entry from the dictionary                        |

表2-8 Python字典提供的方法

| **Method Name** | **Use**            | **Explanation**                                              |
| --------------- | ------------------ | ------------------------------------------------------------ |
| `keys`          | `adict.keys()`     | Returns the keys of the dictionary in a dict_keys object     |
| `values`        | `adict.values()`   | Returns the values of the dictionary in a dict_values object |
| `items`         | `adict.items()`    | Returns the key-value pairs in a dict_items object           |
| `get`           | `adict.get(k)`     | Returns the value associated with `k`, `None` otherwise      |
| `get`           | `adict.get(k,alt)` | Returns the value associated with `k`, `alt` otherwise       |

Defautdict

```python
from collections import defaultdict

# 使用 int 作为工厂函数，适用于计数
count_dict = defaultdict(int)
count_dict['apple'] += 1
print(count_dict['apple'])  # 输出: 1
print(count_dict['banana'])  # 输出: 0，注意这里'banana'之前未定义

# 使用 list 作为工厂函数，适用于存储分组信息
group_dict = defaultdict(list)
group_dict['fruits'].append('apple')
group_dict['fruits'].append('banana')
print(group_dict['fruits'])  # 输出: ['apple', 'banana']
print(group_dict['vegetables'])  # 输出: []，空列表
```

**应用场景**

- **计数**：例如统计文档中每个单词出现的次数。
- **分组**：例如将数据按某个属性分组。

##### 



### 二、二分法、倒排索引

取mid==(l+r)//2时，左端点取“能取到的下限”，右端点取“能取到的上限+1”

while l<r-1:    如果能行l=mid 不能行r=mid

二分+贪心题目类型，需要掌握了。这类问题通常涉及求解最小化最大值（minMax）或最大化最小值（maxMin）。

倒排索引：文档到标记的映射被称为**正排索引**，而从标记指向包含该标记的文档（例如：标记 -> 文档_i, 文档_j, ...）的映射则被称为**倒排索引**！

### 三、链表

知道是存储值，next指针指向下一个就行

## 四、栈

#### 关于栈使用的重要原则

1. **栈的基本用途是用于“等待”**。具体来说，当遇到一条指令，而这条指令的操作依赖于后续的指令时，可以选择将这条指令先入栈，“稍作等待”，直到遍历到后面部分了解到具体如何操作后再利用`pop`方法回过头来处理该指令。这是栈使用的总体原则。
2. **栈与括号匹配的关系密切**。很多涉及栈的问题都涉及到括号匹配问题，其核心在于识别一对括号内所包含的内容。这时同样可以应用第一条原则。当我们遇到左括号时，由于不清楚它对应的右括号在哪里，所以先将其入栈。等到遇到右括号时，再回头找到匹配的左括号，并进行相应的处理。
3. **理解栈相关问题时，研究给定示例非常重要**。在解决栈相关的问题之前，先大致研究一下给出的示例，分析答案和输入数据（或称“密文”）之间的关系非常有帮助。例如，在中序表达式转后序表达式的题目中，通过观察转换后的结果可以发现数字的顺序保持不变，而对于每一个运算单元，符号总是位于最后。这表明：数字不需要入栈，因为它们的操作不依赖于后续的指令，可以直接添加到结果中。相反，运算符需要入栈，因为我们尚未确定该运算符所属的运算单元将在何处结束。一旦根据某些条件判断出运算单元结束，就可以有序地将运算符从栈中弹出，并加入到结果中。

## 五、树

与递归紧密结合！！！

#### 1. 节点定义：

```python
#多叉树
class Node: 
	def __init__(self,data): 
		self.data=data 
		self.children=[]
#二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

#### 2. 建树

```python
#类似邻接表
#第一行是一个整数n，表示二叉树的结点个数。二叉树结点编号从1到n，根结点为1，n <= 10 接下来有n行，依次对应二叉树的n个节点。 每行有两个整数，分别表示该节点的左儿子和右儿子的节点编号。如果第一个（第二个）数为-1则表示没有左（右）儿子
def build_tree(nodes):
    if not nodes:
        return None

    tree_nodes = [None] * (len(nodes) + 1)
    for i in range(1, len(nodes) + 1):
        tree_nodes[i] = TreeNode(i)

    for i, (left, right) in enumerate(nodes, start=1):
        if left != -1:
            tree_nodes[i].left = tree_nodes[left]
        if right != -1:
            tree_nodes[i].right = tree_nodes[right]

    return tree_nodes[1]

def main():
    n = int(input())
    nodes = []
    index = 1
    for _ in range(n):
        left, right = map(int, input().split())
        nodes.append((left, right))
#完全二叉树建树
n = int(input())
a = list(map(int, input().split()))
node = []
for i in range(n):
    node.append(Node(a[i]))
for i in range(n):
    if 0 <= 2 * i + 1 < n: node[i].left = node[2 * i + 1]
    if 0 <= 2 * i + 2 < n: node[i].right = node[2 * i + 2]
```

#### 3. 一些名词

前中后序遍历：根左右、左根右、左右根    层序遍历：按层从左到右

平衡二叉树：左右子树高度差不超过1

BST，二叉搜索（查找，检索，排序）树，

#### 4. 树的表示方法

1. 括号嵌套：先将根结点放入一对圆括号中，然后把它的子树按由左而右的顺序放入括号中，而对子树也采用同样方法处理：同层子树与它的根结点用圆括号括起来，同层子树之间用逗号隔开，最后用闭括号括起来。

   ```
   A(B(*,C),D(E,*))
   ```

2. 树形表示：对二叉树做如下处理，将二叉树的空结点用·补齐，扩展二叉树的先序和后序序列能唯一确定其二叉树。

3. 邻接表表示法（Adjacency List Representation）是一种常见的树的表示方法，特别适用于表示稀疏树（树中节点的度数相对较小）。在邻接表表示法中，使用一个数组来存储树的节点，数组中的每个元素对应一个节点。对于每个节点，使用链表或数组等数据结构来存储它的子节点。

#### 5. 解析树

将表达式建成树的形式！ 比如后序表达式等等

#### 6. Huffman编码

Huffman code通过使用较短的码字code-word 字符串编码高频字符和较长的码字字符串编码低频字符来节省空间。

```python
import heapq

class Node:
    def __init__(self, weight, char=None):
        self.weight = weight
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.weight == other.weight:
            return self.char < other.char
        return self.weight < other.weight

def huffman_encoding(char_freq):
    heap = [Node(freq, char) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.weight + right.weight, min(left.char, right.char))
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def external_path_length(node, depth=0):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return depth * node.weight
    return (external_path_length(node.left, depth + 1) +
            external_path_length(node.right, depth + 1))

def main():
    char_freq = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 8, 'f': 9, 'g': 11, 'h': 12}
    huffman_tree = huffman_encoding(char_freq)
    external_length = external_path_length(huffman_tree)
    print("The weighted external path length of the Huffman tree is:", external_length)

if __name__ == "__main__":
    main()

# Output:
# The weighted external path length of the Huffman tree is: 169
```

例题：构造一个具有n个外部节点的扩充二叉树，每个外部节点Ki有一个Wi对应，作为该外部节点的权。使得这个扩充二叉树的叶节点带权外部路径长度总和最小：

第一行输入一个整数n，外部节点的个数。第二行输入n个整数，代表各个外部节点的权值。 2<=N<=100

```python
import heapq

def min_weighted_path_length(n, weights):
    heapq.heapify(weights)
    total = 0
    while len(weights) > 1:
        a = heapq.heappop(weights)
        b = heapq.heappop(weights)
        combined = a + b
        total += combined
        heapq.heappush(weights, combined)
    return total

# 读取输入
n = int(input())
weights = list(map(int, input().split()))
print(min_weighted_path_length(n, weights))
```

#### 7. 堆 heap

import heap

在实现二叉堆时，我们通过创建一棵**完全二叉树complete binary tree**来维持树的平衡。在完全二叉树中，除了最底层，其他每一层的节点都是满的。

堆的有序性是指：对于堆中任意元素 x 及其父元素 p， p 都不大于 x。

#### 8. 二叉搜索树

二叉搜索树依赖于这样一个性质：小于父节点的键都在左子树中，大于父节点的键则都在右子树中。我们称这个性质为二叉搜索性。

同一个序列二叉搜索树有很多种，不唯一。二叉搜索树可以实现快速排序

平衡因子是指节点的左子树高度与右子树高度之差的绝对值。将平衡因子为-1、0和1的树都定义为**平衡树**

#### 9. 并查集

```python
def find(x):
    if parent[x] != x: # 如果不是根结点，继续循环
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y) #这样也只能把x这条路上的点给重置了，别的点可能还没归到y去，再使用时还需要重新find！
```

基本原理： 管理元素分组： 1. 支持操作： find(x)：查找根节点（代表元） union(x,y)：合并两个集合 2. 优化： 路径压缩：find时扁平化树结构 按秩合并：小树合并到大树 应用场景：连通分量检测、图算法

```python
class DisjSet:
	def __init__(self, n):
		# Constructor to create and initialize sets of n items
		self.rank = [1] * n
		self.parent = [i for i in range(n)]


	# Finds set of given item x
	def find(self, x):
		
		# Finds the representative of the set that x is an element of
		if (self.parent[x] != x):
			
			# if x is not the parent of itself
			# Then x is not the representative of its set
			self.parent[x] = self.find(self.parent[x])
			
			# so we recursively call Find on its parent
			# and move i's node directly under the
			# representative of this set

		return self.parent[x]


	# Do union of two sets represented by x and y.
	def Union(self, x, y):
		
		# Find current sets of x and y
		xset = self.find(x)
		yset = self.find(y)

		# If they are already in same set
		if xset == yset:
			return

		# Put smaller ranked item under
		# bigger ranked item if ranks are different
		if self.rank[xset] < self.rank[yset]:
			self.parent[xset] = yset

		elif self.rank[xset] > self.rank[yset]:
			self.parent[yset] = xset

		# If ranks are same, then move y under x (doesn't matter
    # which one goes where) and increment rank of x's tree
		else:
			self.parent[yset] = xset
			self.rank[xset] = self.rank[xset] + 1

# Driver code
obj = DisjSet(5)
obj.Union(0, 2)
obj.Union(4, 2)
obj.Union(3, 1)
if obj.find(4) == obj.find(0):
	print('Yes')
else:
	print('No')
if obj.find(1) == obj.find(0):
	print('Yes')
else:
	print('No')


"""
Yes
No
"""
```



#### 10. 前缀树（字典树）Trie

```python
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

```

## 六、图

#### 1. 图的实现

有两种非常著名的图实现，它们分别是邻接矩阵 **adjacency matrix** 和邻接表**adjacency list**。dict套list, dict套queue，dict套dict，真好用！

dict的value如果是list/set，是邻接表。dici嵌套dict 是 字典树/前缀树/Trie

邻接矩阵适用于表示有很多条边的图。

在邻接表实现中，我们为图对象的所有顶点保存一个主列表，同时为每一个顶点对象都维护一个列表，其中记录了与它相连的顶点。在对Vertex类的实现中，我们使用字典（而不是列表），字典的键是顶点，值是权重。在机考中，也可以直接使用**二维列表或者字典来表示邻接表**。

```python
#节点为数字的图的邻接表：
n,m=map(int,input().split())
g=defaultdict(list)
for i in range(m):
    x,y=map(int,input().split())
    g[x].append(y)
    g[y].append(x)
    '''maps[x].append((y, d))
    maps[y].append((x, d))'''
#
```



#### 2. DFS & BFS

熟练掌握！

#### 3. 拓扑排序

拓扑排序（Topological Sorting）是对有向无环图（DAG）进行排序的一种算法。它将图中的顶点按照一种线性顺序进行排列，使得对于任意的有向边 (u, v)，顶点 u 在排序中出现在顶点 v 的前面。

Kahn算法的基本思想是通过不断地移除图中的入度为0的顶点，并将其添加到拓扑排序的结果中，直到图中所有的顶点都被移除。

#### 4. 强连通单元

Kosaraju算法是一种用于在有向图中寻找强连通分量（Strongly Connected Components，SCC）的算法。它基于深度优先搜索（DFS）和图的转置操作。

Kosaraju算法的核心思想就是两次深度优先搜索（DFS）。

1. **第一次DFS**：在第一次DFS中，我们对图进行标准的深度优先搜索，但是在此过程中，我们记录下顶点完成搜索的顺序。这一步的目的是为了找出每个顶点的完成时间（即结束时间）。
2. **反向图**：接下来，我们对原图取反，即将所有的边方向反转，得到反向图。
3. **第二次DFS**：在第二次DFS中，我们按照第一步中记录的顶点完成时间的逆序，对反向图进行DFS。这样，我们将找出反向图中的强连通分量。

使用stack模拟按照结束时间的递减顺序访问顶点。

#### 5. 最短路算法

##### 5.1 Dijkstra

类似bfs：使用距离作为优先队列（最小堆heap）的键，每次弹出距离最小的，对其相邻点进行更新：如果更短，将到达w的距离更新为更短的值，并且将w的前驱顶点从u改为x。

Dijkstra算法只适用于边的权重均为正的情况

```python
import heapq
def dijkstra(graph, start):
    n = len(graph)
    distances = {node: float('inf') for node in range(n)}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
        	continue
        for neighbor, weight in graph[current_node]:
        	distance = current_distance + weight
        	if distance < distances[neighbor]:
        		distances[neighbor] = distance
        		heapq.heappush(priority_queue, (distance, neighbor))
    return distances
graph = {
0: [(1, 4), (2, 1)],
1: [(3, 1)],
2: [(1, 2), (3, 5)],
3: []
}
start_node = 0
print(dijkstra(graph, start_node)) # 输出: {0: 0, 1: 3, 2: 1, 3: 4}
```



##### 5.2 多源最短路径Floyd-Warshall算法

求解所有顶点之间的最短路径可以使用**Floyd-Warshall算法**，它是一种多源最短路径算法。Floyd-Warshall算法可以在有向图或无向图中找到任意两个顶点之间的最短路径。

- **思想**：动态规划 + 三重循环

- 转移方程：

  `dist[i][j]=min⁡(dist[i][j], dist[i][k]+dist[k][j])`

  表示是否通过中间点 k 能让路径更短

  以下是一个使用Floyd-Warshall算法求解所有顶点之间最短路径的示例代码：

  ```python
  def floyd_warshall(graph):
      n = len(graph)
      dist = [[float('inf')] * n for _ in range(n)]
  
      for i in range(n):
          for j in range(n):
              if i == j:
                  dist[i][j] = 0
              elif j in graph[i]:
                  dist[i][j] = graph[i][j]
  
      for k in range(n):
          for i in range(n):
              for j in range(n):
                  dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  
      return dist
  ```

  

  在上述代码中，`graph`是一个字典，用于表示图的邻接关系。它的键表示起始顶点，值表示一个字典，其中键表示终点顶点，值表示对应边的权重

#### 6.最小生成树

##### 6.1 Prim算法

从一个顶点开始，使用最小堆，每次弹出最短的路径进行扩展，直到所有顶点都被加入最小生成树中

```python
#兔子和星空
import heapq
n = int(input())
graph = [[] for i in range(n)]
for i in range(n - 1):
    x = list(input().split())
    for j in range(int(x[1])):
        graph[ord(x[0]) - 65].append((ord(x[2 + j * 2]) - 65, int(x[2 + j * 2 + 1])))  # ord('A')==65
        graph[ord(x[2 + j * 2]) - 65].append((ord(x[0]) - 65, int(x[2 + j * 2 + 1])))
#print(graph)
ans=0
h=[(0,0)]
v=[0]*n
while h:
    lth,star=heapq.heappop(h)
    if v[star]==0:
        ans+=lth
        v[star]=1
        for x in graph[star]:
            heapq.heappush(h,(x[1],x[0]))
print(ans)

```



##### 6.2 Kruskal算法

将所有边排序，从最小的开始，对其顶点进行连接，同时使用并查集结构，如此反复直到所有顶点连成一个集合

下面是一个使用Kruskal算法求解最小生成树的示例代码：

```python
class DisjointSet:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))
        self.rank = [0] * num_vertices

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1


def kruskal(graph):
    num_vertices = len(graph)
    edges = []

    # 构建边集
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    # 按照权重排序
    edges.sort(key=lambda x: x[2])

    # 初始化并查集
    disjoint_set = DisjointSet(num_vertices)

    # 构建最小生成树的边集
    minimum_spanning_tree = []

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            minimum_spanning_tree.append((u, v, weight))

    return minimum_spanning_tree
```

### 小结

介绍了图的抽象数据类型，以及一些实现方式。如果能将一个问题用图表示出来，那么就可以利用图算法加以解决。对于解决下列问题，图非常有用。

❏ 利用宽度优先搜索找到无权重的最短路径。 ❏ 利用Dijkstra算法求解带权重的最短路径。 ❏ 利用深度优先搜索来探索图。 ❏ 利用强连通单元来简化图。 ❏ 利用拓扑排序为任务排序。 ❏ 利用最小生成树广播消息。

## 七、KMP

实现线性复杂度的字符串匹配算法！KMP（Knuth-Morris-Pratt）算法是一种利用双指针和动态规划的字符串匹配算法。

```python
""""
compute_lps 函数用于计算模式字符串的LPS表。LPS表是一个数组，
其中的每个元素表示模式字符串中当前位置之前的子串的最长前缀后缀的长度。
该函数使用了两个指针 length 和 i，从模式字符串的第二个字符开始遍历。
"""
def compute_lps(pattern):
    """
    计算pattern字符串的最长前缀后缀（Longest Proper Prefix which is also Suffix）表
    :param pattern: 模式字符串
    :return: lps表
    """

    m = len(pattern)
    lps = [0] * m  # 初始化lps数组
    length = 0  # 当前最长前后缀长度
    for i in range(1, m):  # 注意i从1开始，lps[0]永远是0
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]  # 回退到上一个有效前后缀长度
            '''
            例如要acacbaca a
                 00120123 
            直接加a不行，那么回退，最后又前面一段加上最后一个字符pattern[i] 等于开头段，则相当于找目前0:length这段的前缀！
            '''
        if pattern[i] == pattern[length]:
            length += 1
        lps[i] = length

    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    lps = compute_lps(pattern)
    matches = []

    # 在 text 中查找 pattern
    j = 0  # 模式串指针
    for i in range(n):  # 主串指针
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]  # 模式串回退
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - j + 1)  # 匹配成功
            j = lps[j - 1]  # 查找下一个匹配

    return matches


text = "ABABABABCABABABABCABABABABC"
pattern = "ABABCABAB"
index = kmp_search(text, pattern)
print("pos matched：", index)
# pos matched： [4, 13]

```

