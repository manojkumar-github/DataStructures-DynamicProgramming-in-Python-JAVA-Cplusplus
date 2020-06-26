#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only


from plan.data_structures.graph.representation import Graph


def bfs(graph, first_vertex):

    visited = [False] * graph.num_vertices

    visited[first_vertex] = True
    queue = [first_vertex]
    print(first_vertex)
    while queue:
        curr_vertex = queue.pop(0)
        connections = graph.vertices_map[curr_vertex].get_connections()
        for connected_vertex in connections:
            if visited[connected_vertex] != True:
                visited[connected_vertex] = True
                queue.append(connected_vertex)
                print( connected_vertex)


def dfs_util(graph , current_vertex, visited):

    print(current_vertex)
    visited[current_vertex] = True
    connected_vertices = graph.vertices_map[current_vertex].get_connections()
    for connected_vertex in connected_vertices:
        if visited[connected_vertex] == False:
            dfs_util(graph, connected_vertex, visited)

def dfs(graph, start_vertex):
    visited = [False] * graph.num_vertices
    dfs_util(graph, start_vertex, visited)







def shortest_path_util(graph, src, dest, visited):
    if src == dest:
        return 0

    connected_vertices = graph.vertices_map[src].get_connections()
    if dest in connected_vertices:
        return 1
    else:
        atmost = graph.num_vertices
        for connected_vertex in connected_vertices:
            if visited[connected_vertex] != True:
                visited[connected_vertex] = True
                this_path_distance = shortest_path_util(graph, connected_vertex,
                                                      dest, visited)
                if this_path_distance < atmost:
                    atmost = this_path_distance
        return 1 + atmost

def shortest_path(graph, src, dest):

    visited = [False] * graph.num_vertices
    visited[src] = True
    return shortest_path_util(graph, src, dest, visited)







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

#bfs(g, 0)
#dfs(g, 0)
print(shortest_path(g, 0, 2))