"""
1. Boolean array to track visited
2. defaultdict implementation
"""

from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src_node, dest_node):
        self.graph[src_node].append(dest_node)

    def dfs_util(self, curr_vertex, visited):
        visited[curr_vertex] = True
        print(curr_vertex)
        for connected_vertex in self.graph[curr_vertex]:
            if not visited[connected_vertex]:
                self.dfs_util(connected_vertex, visited)

    def print_dfs_graph(self, src_node):
        visited = [False] * len(self.graph)
        self.dfs_util(src_node, visited)




if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("Following is Depth First Traversal"
          " (starting from vertex 2)")
    g.print_dfs_graph(2)