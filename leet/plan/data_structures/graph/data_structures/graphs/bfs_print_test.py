from collections import defaultdict



class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, node):
        self.graph[src].append(node)

    def print_bfs_graph(self, src_node):
        visited = [False] * len(self.graph)
        my_queue = []
        my_queue.append(src_node)
        visited[src_node] = True # do not forget

        while my_queue:
            cur_vertex = my_queue.pop(0)
            print(cur_vertex, end=" ")
            for connected_vertext in self.graph[cur_vertex]:
                if visited[connected_vertext]:
                    continue
                visited[connected_vertext] = True
                my_queue.append(connected_vertext)

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