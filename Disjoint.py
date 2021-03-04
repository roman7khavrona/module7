def __add__(self, other: "Graph") -> "Graph":
        """
        Make a disjoint union of two graphs.
        :param other: Graph to add to `self'.
        :return: New graph which is a disjoint union of `self' and `other'.
        """
        disjoint_union = Graph(directed=False)
        vertices = self.vertices + other.vertices
        edges = []
        map_vertices = dict()
        for vertex in vertices:
            map_vertices[vertex] = Vertex(graph=disjoint_union)
        done = []
        for vertex in map_vertices:
            done.append(vertex)
            for neighbour in vertex.neighbours:
                if neighbour not in done:
                    edges.append(Edge(map_vertices[vertex], map_vertices[neighbour]))
        for vertex in map_vertices.values():
            disjoint_union.add_vertex(vertex)
        for edge in edges:
            disjoint_union.add_edge(edge)
        return disjoint_union