import sys

from Models.graph import Graph

from GUI.gui import DrawGraph


# function to check if values are binary matrix or not 
def is_valid_values(values):
    
    for value in values:

        if int(value) not in [0, 1] : return False

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
    for parent, row in enumerate(matrix):
        
        children = [index for index, child in enumerate(row) if child == '1']

        graph.connect(parent, tuple(children))

    print("connected" if graph.is_connected() else "sorry")

    # Draw graph
    drawgraph = DrawGraph(graph)
    drawgraph.draw()



# Tell python to run main method
if __name__ == "__main__": main()