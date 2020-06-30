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
    def is_connected(self):

        return True if self.bfs() else False


    # Breadth-first search (BFS)
    def bfs(self):

        visited, queue = list(), list() # List to keep track of visited and queue nodes

        VMN = sorted(                                # The vertice with most neighbors
            
            self.graph_dict.keys(),

            key=lambda x:len(self.graph_dict[x]),

            reverse = True
        )[0]

        visited.append(VMN)

        queue.append(VMN)

        while queue:

            start = queue.pop(0)

            print(start, end = ' ')

            neighbours = self.get_neighbors(start)
            
            for neighbour in neighbours:

                if neighbour not in visited:

                    visited.append(neighbour)

                    queue.append(neighbour)

            if set(visited) == set(self.get_vertices()): return True

        return False