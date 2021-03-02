class Graph:

    def __init__(self, vertices):
        self.num_v = vertices
        self.graph = []

    def addEdge(self, a, b, w):
        self.graph.append([a, b, w])

    def get_label(self, forest, vertex):
        if forest[vertex] == vertex:
            return vertex
        return self.get_label(forest, forest[vertex])

    def boruvka(self):
        # Initialize a forest to be a set of one-vertex trees,
        # one for each vertex of the graph, G.
        forest = [node for node in range(self.num_v)]
        rank = [0] * self.num_v
        # Initial components in the graph is number of vertices.
        components = self.num_v
        mstweight = 0
        # Initialize the cheapest edge for each component to None
        cheapest = [None] * self.num_v
        mst = []
        while components > 1:
            # Traverse through each edge in the graph
            for edge in range(len(self.graph)):
                # Find the connected components of the edge, and label
                # each vertex of G by its component.
                print("Edge Selected:", self.graph[edge])
                a, b, w = self.graph[edge]
                comp_one = self.get_label(forest, a)
                comp_two = self.get_label(forest, b)
                print("Component 1:", comp_one)
                print("Component 2:", comp_two)
                # If u and v have different component labels, set cheapest
                # edge of component.
                #!!! if components are the same, then the edge belongs to the
                # same component, so therefore it does not need to be set
                if comp_one != comp_two:
                    if cheapest[comp_one] == None or cheapest[comp_one][2] > w:
                        cheapest[comp_one] = [a,b,w]
                    if cheapest[comp_two] == None or cheapest[comp_two][2] > w:
                        cheapest[comp_two] = [a,b,w]
            # For each component that has a cheapest edge, add the edge to
            # the forest, F.
            for node in range(self.num_v):
                # Check if a cheapest node exists for this node
                print("\nForest", forest)
                print("Cheapest", cheapest)
                print("Rank", rank)
                if cheapest[node] != None:
                    a, b, w = cheapest[node]
                    comp_one = self.get_label(forest, a)
                    comp_two = self.get_label(forest, b)
                    print("Node:", cheapest[node])
                    print("Comp_one:", comp_one)
                    print("Comp_two:", comp_two)
                    # Attach the smaller ranking tree under the root of the
                    # higher ranking tree.
                    if comp_one != comp_two:
                        # Add the weight of the edge to the total weight of the
                        # minimum spanning tree.
                        mstweight += w
                        # Get the root label of each of the components
                        xroot = self.get_label(forest, comp_one)
                        yroot = self.get_label(forest, comp_two)
                        print("X:", xroot, "Y:", yroot)
                        # Selected edge is added to the MST list_
                        selected_edge = ("Added Edge %d-%d (%d)" % (a,b,w))
                        if selected_edge in mst:
                            mstweight -= w
                            continue
                        print(selected_edge, "\n")
                        mst.append(str(selected_edge))
                        forest[yroot] = xroot
                        # As a component has been selected and joined with
                        # another component, it is decremented
                        components = components - 1
            # Reset the cheapest edge for each component to None
            cheapest = [None] * self.num_v
        return mstweight, mst



if __name__ == "__main__":
    undirected_graph = Graph(4)
    undirected_graph.addEdge(0, 1, 10)
    undirected_graph.addEdge(0, 2, 6)
    undirected_graph.addEdge(0, 3, 5)
    undirected_graph.addEdge(1, 3, 15)
    undirected_graph.addEdge(2, 3, 4)

    weight, mstree = undirected_graph.boruvka()
    [print(edge) for edge in mstree]
    print("Minimum Spanning Tree Weight:", weight)

    undirected_graph2 = Graph(9)
    undirected_graph2.addEdge(0, 1, 4)
    undirected_graph2.addEdge(0, 7, 8)
    undirected_graph2.addEdge(1, 7, 11)
    undirected_graph2.addEdge(1, 2, 8)
    undirected_graph2.addEdge(7, 8, 7)
    undirected_graph2.addEdge(6, 7, 1)
    undirected_graph2.addEdge(2, 8, 2)
    undirected_graph2.addEdge(2, 3, 7)
    undirected_graph2.addEdge(6, 8, 6)
    undirected_graph2.addEdge(5, 6, 2)
    undirected_graph2.addEdge(2, 5, 4)
    undirected_graph2.addEdge(3, 4, 9)
    undirected_graph2.addEdge(3, 5, 14)
    undirected_graph2.addEdge(4, 5, 10)

    weight, mstree = undirected_graph2.boruvka()
    [print(edge) for edge in mstree]
    print("Minimum Spanning Tree Weight:", weight)
