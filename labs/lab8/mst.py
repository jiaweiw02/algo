class Graph:
    def __init__(self, num_vertices, union_set=None):
        self.num_vertices = num_vertices
        self.edges = []
        self.union_set = set(union_set) if union_set is not None else None

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def find(self, parent, me):
        if parent[me] == me:
            return me
        return self.find(parent, parent[me])

    def union(self, parent, rank, x, y):
        x_parent = self.find(parent, x)
        y_parent = self.find(parent, y)

        if rank[x_parent] < rank[y_parent]:
            parent[x_parent] = y_parent
        elif rank[y_parent] < rank[x_parent]:
            parent[y_parent] = x_parent
        else:
            parent[y_parent] = x_parent
            rank[x_parent] += 1

    def kruskal(self, table):
        result = []
        self.edges.sort(key=lambda item: item[2])
        parent = [i for i in range(self.num_vertices)]
        rank = [0 for i in range(self.num_vertices)]
        connections = [0 for i in range(self.num_vertices)]

        i, e = 0, 0
        while e < self.num_vertices - 1:
            if i >= len(self.edges):
                print("not possible")
                return
            u, v, w = self.edges[i]  # fail

            x = self.find(parent, u)
            y = self.find(parent, v)
            i = i + 1

            if x == y:
                continue

            if u in self.union_set:
                if connections[u] != 0:
                    continue
                connections[u] = 1
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

            elif v in self.union_set:
                if connections[v] != 0:
                    continue
                connections[v] = 1
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

            else:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        for u, v, weight in result:
            print("{} - {}: {}".format(table[u], table[v], weight))


A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
H = 7
I = 8

table = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I" }

g = Graph(9, [A, E, F])
g.add_edge(A, B, 10)
g.add_edge(A, C, 12)
g.add_edge(B, C, 9)
g.add_edge(B, D, 8)
g.add_edge(C, E, 3)
g.add_edge(C, F, 1)
g.add_edge(D, E, 7)
g.add_edge(D, G, 8)
g.add_edge(D, H, 5)
g.add_edge(E, F, 3)
g.add_edge(F, H, 6)
g.add_edge(G, H, 9)
g.add_edge(G, I, 2)
g.add_edge(H, I, 11)
# g.add_edge(E, G, 2)  # added edge
g.kruskal(table)
