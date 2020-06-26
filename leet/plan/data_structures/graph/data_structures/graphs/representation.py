class AdjNode(object):
    """
    A class to represent the adjacent list of nodes
    """
    def __init__(self, data):
        """

        :param data: data at the node
        """
        self.vertex = data
        # we can add a new attribute called weight like self.weight
        self.next = None # we can map a dict with value and weight

class Graph(object):
    """
    A class to represent the graph . A graph is an list of adjacent lists
    """
    def __init__(self, n_vertices):
        """

        :param n_vertices: Number of vertices in the graph
        """
        self.V  = n_vertices
        # each array element in the below list represent the list of
        # adjacent vertices
        self.graph = [None] * self.V # [None, None, None...]

    def add_edge(self, src, dest):
        """

        :param src: an integer value which is an index of the graph list
        :param dest: an integer value
        :return: None
        """
        # adding the node to the source node
        dest_node = AdjNode(dest) # creates a node
        dest_node.next = self.graph[src] # map the "src" value to the new
        # dest node next
        self.graph[src] = dest_node

        # adding the source node to the destination as it is undirected graph
        src_node = AdjNode(src)
        src_node.next = self.graph[dest]
        self.graph[dest] = src_node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {} \n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print("---> {}".format(temp.vertex), end="")
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



