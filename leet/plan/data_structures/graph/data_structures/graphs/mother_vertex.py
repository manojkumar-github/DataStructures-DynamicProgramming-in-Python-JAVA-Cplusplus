from collections import defaultdict

class Graph:
    def __init__(self, n_vertices):
        self.graph = defaultdict(list)
        self.V = n_vertices

    def add_edge(self, src_node, dest_node):
        self.graph[src_node].append(dest_node)

    """
    Case 1: Undirected Connected graph: all are mother vertices
    Case 2: Undirected/Directed Disconnected graph: No mother vertices
    Case 3: Directed Connected Graph - possible
    Navie Approach: Using BFS/DFS search
    Better Approach: Kosaraju's Strongly Connected Algorithm
        Idea: Mother Vertex has maximum finish time
    """

    def dfs_util(self, curr_vertex, visited):
        visited[curr_vertex] = True
        for connected_vertex in visited[curr_vertex]:
            if visited[curr_vertex] == False:
                self.dfs_util(curr_vertex, visited)

    def find_mother(self):

        visited = [False] * self.V

        last_finished_vertex = None

        for curr_vertex in range(self.V):
            if visited[curr_vertex] == False:
                self.dfs_util(curr_vertex, visited)
                last_finished_vertex = curr_vertex
        """
        If there exits mother vertex in given graph then v must be one
        now check if curr_vertex is actually a mother vertex 
        """

        visited = [False] * self.V
        self.dfs_util(curr_vertex, visited)
        if any(curr_vertex == False for curr_vertex in visited):
            return None
        else:
            return curr_vertex

