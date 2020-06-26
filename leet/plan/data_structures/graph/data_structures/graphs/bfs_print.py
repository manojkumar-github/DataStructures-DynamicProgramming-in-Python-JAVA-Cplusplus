"""
BFS - Breadth First Search
1) In graphs - we may visit same node more than once
2) Use a boolean array
3) DefaultDict - Representation
"""

from collections import defaultdict

class Graph(object):
    def __init__(self):
        # default dictionary to store graphs
        self.graph = defaultdict(list)

    def add_edge(self, src, node):
        self.graph[src].append(node)

    def print_bfs_graph(self, src_node):

        visited = [False] * len(self.graph)

        # create a queue for BFS
        my_queue = list()
        # Mark the source node as visited and enqueue it
        my_queue.append(src_node)
        visited[src_node] = True

        while my_queue:
            # Dequeue a vertext from  queue and print it
            cur_vertex = my_queue.pop(0)
            print(cur_vertex, end= " ")
            # Get all the adjacent vertices of the dequeue vertex
            for connected_vertex in self.graph[cur_vertex]:
                if visited[connected_vertex] == False:
                    visited[connected_vertex] = True
                    my_queue.append(connected_vertex)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.print_bfs_graph(2)