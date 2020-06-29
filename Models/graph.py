import sys


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

            neighbours = self.get_neighbors(start)
            
            for neighbour in neighbours:

                if neighbour not in visited:

                    visited.append(neighbour)
                    queue.append(neighbour)

            if set(visited) == set(self.get_vertices()): return True

        return False


# function to check if values are binary matrix or not 
def is_valid_values(values):

    for value in values:

        if not (int(value) != 0 or int(value) != 1): return False

    return True


# Main function
def main():


    try:

        num_of_vertics = int(input('The number of vertics: '))

        try:

            matrix = list()

            for num in range(num_of_vertics):

                input_tmp = list(input('{}. '.format(num + 1)).lower().split(" "))

                while '' in input_tmp: input_tmp.remove('')
                
                if not is_valid_values(input_tmp): raise ValueError

                if len(input_tmp) > num_of_vertics:
                    
                    sys.exit("The number of vertics can't be more than {}".format(num_of_vertics))

                if input_tmp.count('1') >= num_of_vertics:

                    sys.exit("The number of connected vertics can't be equal or more than {}".format(num_of_vertics))


                matrix.append(tuple(input_tmp))

        except (ValueError, NameError, SyntaxError):          # raise error message if matrix rows values are not binary and exit
            
            sys.exit("Matrix Values must be binary!")
        
    except (ValueError, NameError, SyntaxError):               # raise error message if num_of_vertics is not integer and exit

        sys.exit('Not an integer! Please enter an integer.')

    # Create a graph
    graph = Graph()
    
    # Create graph connections
    for row_index, row in enumerate(matrix):
        
        children = [index for index, child in enumerate(row) if child == '1']

        graph.connect(row_index, tuple(children))

    print("connected" if graph.is_connected() else "sorry")


# Tell python to run main method
if __name__ == "__main__": main()