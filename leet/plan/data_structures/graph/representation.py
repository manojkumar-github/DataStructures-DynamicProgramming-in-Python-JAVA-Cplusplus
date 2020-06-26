#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
1. Graph consists of nodes
2. Edges (u,v) != (v,u) in directed graphs
3. Representation : Adjacency matrix vs Adjacency list

Adjacency matrix:
    Pros:
        - Removing an element takes O(1) time
        - check if edge exists takes O(1) time
    Cons:
        - More space O(n^2)


Graph:

Verti
"""

class Vertex:
    def __init__(self, key):
        self.key = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_key(self):
        return self.key

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vertices_map = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vertices_map[key] = new_vertex

    def get_vertex(self, key):
        if key in self.vertices_map:
            return self.vertices_map[key]
        else:
            return None

    def add_edge(self, src, dest, weight=0):
        if src not in self.vertices_map:
            self.add_vertex(src)
        if dest not in self.vertices_map:
            self.add_vertex(dest)
        self.vertices_map[src].add_neighbor(dest, weight=weight)

    def get_vertices(self):
        return self.vertices_map.keys()

if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for v in g.vertices_map:
        print(v, g.vertices_map[v].get_connections())
        for w in g.vertices_map[v].get_connections():
            print("( %s , %s )" % (g.vertices_map[v].get_key(), g.vertices_map[w].get_key()))
        print("###############")



