"""
-   Graph consists a finite set of vertices(in non-graphical language, nodes) and
    a set of edges which connect a pair of vertices.

    -   Why we need them?
        - They're used to represent networks.

    - Terminlogy:
        - Vertices: Vertices are the nodes in graph language.
        - Edge: The edge is the line that connects pairs of vertices.
        - Unweighted graph: A graph which does not have a weigh associated with any edge.
        - Weighted graph: A graph which has a weight associated with any edge.
        - Undirected graph: In case the edges of the graph do not have direction associated with them.
        - Directed graph: If the edges in a graph have direction associated with them.
        - Cyclic graph: A graph which has a least one loop.
        - Acyclic graph: A graph with no loop.
        - Tree: It is a special case of directed acyclic graph.
    
    - Types:
        - Graph
            -- Directed
                -- Weighted
                    -- Positive
                    -- Negative
                -- Unweighted
            -- Undirected
                -- Weighted
                    -- Positive
                    -- Negative
                -- Unweighted
    - Representation:
        - Adjacency Matrix: an adjacency matrix is a square matrix or you can
          say it is a 2D array. And the elements of the matrix indicate
          whether pairs of vertices are adjacent or not in the graph.
        - Adjacency List: an adjacency list is a collection of unordered list
          used to represent a graph. Each list describes the set of neighbors
          of a vertex in the graph.
"""


class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_edge(self, vertex, edge):
        self.graph_dict[vertex].append(edge)


if __name__ == "__main__":
    graph_dict = {
        "a": ["b", "c"],
        "b": ["a", "b", "e"],
        "c": ["a", "e"],
        "d": ["b", "e", "f"],
        "e": ["d", "f"],
        "f": ["d", "e"]
    }

    graph = Graph(graph_dict=graph_dict)
    print(graph.graph_dict)
    graph.add_edge("e", "c")
    print(graph.graph_dict)