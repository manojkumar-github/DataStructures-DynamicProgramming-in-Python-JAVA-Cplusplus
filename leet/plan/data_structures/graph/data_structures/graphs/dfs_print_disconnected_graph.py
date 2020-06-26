from collections import defaultdict

class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src_node, dest_node):
        self.graph[src_node].append(dest_node)

    def dfs_util(self, curr_vertex, visited):
        visited[curr_vertex] = True
        print(curr_vertex)
        for connected_vertex in self.graph[curr_vertex]:
            if not visited[connected_vertex]:
                self.dfs_util(connected_vertex, visited)

    def print_dfs_disconnected_graph(self):
        visited = [False] * len(self.graph)
        n_vertices = len(self.graph)

        for i in range(n_vertices):
            if not visited[i]:
                self.dfs_util(i, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.print_dfs_disconnected_graph()

