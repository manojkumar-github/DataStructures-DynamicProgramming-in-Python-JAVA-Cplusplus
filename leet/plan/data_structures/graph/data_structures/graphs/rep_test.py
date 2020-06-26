class AdjNode(object):
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph(object):
    def __init__(self, n_vertices):
        self.V = n_vertices
        self.graph = [None] * self.V

    def add_edge(self, src_index, dest_index):
        # First add the destination node to src node
        dest_node = AdjNode(dest_index)
        dest_node.next = self.graph[src_index]
        self.graph[src_index] = dest_node

        # next add the source node to dest node index list
        # as this is an undirected graph
        src_node = AdjNode(src_index)
        src_node.next = self.graph[dest_index]
        self.graph[dest_index] = src_node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertixes for {} with head".format(i),
                  end="")
            print("\n")
            temp = self.graph[i]
            while temp:
                print("----> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n\n")

if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.print_graph()