import sys


# function to check if values are binary matrix or not 
def is_valid_values(values, num_of_vertics):

    if len(values) > num_of_vertics:
        
        sys.exit("The number of vertics can't be more than {}".format(num_of_vertics))

    if values.count('1') >= num_of_vertics:

        sys.exit("The number of connected vertics can't be equal or more than {}".format(num_of_vertics))
    
    for value in values:

        if int(value) not in [0, 1] : sys.exit("Matrix Values must be binary!")

    return True