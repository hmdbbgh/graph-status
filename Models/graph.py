# This class represent a graph
class Graph:


    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):

        self.graph_dict = graph_dict or {}


    # Add a link from parent to children
    def connect(self, parent, children):

        self.graph_dict.setdefault(parent, children)


    # Get vertices
    def get_vertices(self):

        return self.graph_dict.keys()


    # Get number of vertices
    def get_num_of_vertices(self):

        return len(self.get_vertices())


    # Get neighbors or a neighbor
    def get_neighbors(self, parent):

        return self.graph_dict.get(parent) if parent in self.graph_dict.keys() else None


    # Check if a directed graph is connected or not?
    def is_semi_connected(self):

        matrix = [[False]*self.get_num_of_vertices() for v in range(self.get_num_of_vertices())]

        for vertex in range(self.get_num_of_vertices()):

            matrix[vertex][vertex] = True

            distance = self.bfs(vertex)
            
            for key in distance.keys():

                    if distance[key] != -1:

                        matrix[vertex][key], matrix[key][vertex] = True, True

        return False if list(filter(lambda row: False in row, matrix)) else True    #retun True if graph is semi-connected otherwise False


    # Breadth-first search (BFS)
    def bfs(self, start_vertex):

        visited, queue = list(), list() # List to keep track of visited and queue nodes

        distance = {i:0 for i in range(self.get_num_of_vertices())}

        visited.append(start_vertex)

        queue.append(start_vertex)

        while queue:

            start = queue.pop(0)

            neighbours = self.get_neighbors(start)
            
            for neighbour in neighbours:

                if neighbour not in visited:

                    distance[neighbour] = distance[start] + 1

                    visited.append(neighbour)

                    queue.append(neighbour)

        for vertex in distance.keys():

            if vertex not in visited:

                distance[vertex] = -1

        return distance