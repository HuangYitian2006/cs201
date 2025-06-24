class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def get_neighbor(self, other):
        return self.neighbors.get(other, None)

    def set_neighbor(self, other, weight=0):
        self.neighbors[other] = weight

    def __repr__(self):  # 为开发者提供调试信息
        return f"Vertex({self.key})"

    def __str__(self):  # 面向用户的输出
        return (
                str(self.key)
                + " connected to: "
                + str([x.key for x in self.neighbors])
        )

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_key(self):
        return self.key

class Graph:
    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vertices.get(key, None)

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_vert, to_vert, weight=0):
        if from_vert not in self.vertices:
            self.set_vertex(from_vert)
        if to_vert not in self.vertices:
            self.set_vertex(to_vert)
        self.vertices[from_vert].set_neighbor(self.vertices[to_vert], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

n,m=map(int,input().split())
g=Graph()
for i in range(n):
    g.set_vertex(i)
for _ in range(m):
    x,y=map(int,input().split())
    g.add_edge(x,y)
    g.add_edge(y,x)
ans=[[0]*n for i in range(n)]
for i in range(n):
    ans[i][i]=len(g.vertices[i].neighbors)
for i in range(n):
    for j in range(n):
        if i!=j and g.vertices[j] in g.vertices[i].neighbors:
            ans[i][j]=-1
#print(g.vertices[0].neighbors)
for i in range(n):
    print(*ans[i])
