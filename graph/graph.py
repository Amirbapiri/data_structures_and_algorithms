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

    def bfs(self, vertex):
        """
        BFS is an algorithm for traversing graph data structure. It starts
        at some arbitrary node of a graph and explores the neighbor nodes first,
        before moving to the next level neighbors.

        BSF can be reached through following these steps:
            -   Enqueue any starting vertex
                (any vertex can be a start point since traversing graph
                 means visiting all vertices, as we know, vertices are all connected to eachother somehow.)
            -   while queue is not empty:
                -   next_vertext_to_be_visited = dequeue()
                    if next_vertext_to_be_visited is unvisited:
                        - mark it as visited
                        - enqueue all adjacent
                        - unvisited vertices of next_vertext_to_be_visited

        Time complexity: O(V + E)
        Space complexity: O(V + E)
        """
        visited = [vertex]
        queue = [vertex]

        while queue:
            dequeue = queue.pop(0)
            print(dequeue)
            for adjacent in self.graph_dict[dequeue]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    queue.append(adjacent)

    def dfs(self, vertex):
        """
        DFS is an algorithm for traversing a graph data structure which starts
        selection some arbitrary vertex and explores as far as possible along each edge before backtracking.

        DFS can be reached through following these steps:
            -   Push any starting vertex
            -   While stack is not empty:
                -   vertex_to_be_popped = pop()
                    if vertex_to_be_popped is unvisited:
                        mark it visited
                        push all adjacent
                        unvisited vertices of vertex_to_be_popped

        Time complexity: O(V + E)
        Space complexity: O(V + E)       
        """
        visited = [vertex]
        stack = [vertex]
        while stack:
            vertex_to_pop = stack.pop()
            print(vertex_to_pop)
            for adjacent in self.graph_dict[vertex_to_pop]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    stack.append(adjacent)


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

    print("BFS: ->")
    graph.bfs("a")
    print("DFS: ->")
    graph.dfs("a")
