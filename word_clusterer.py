# Word Clusterer

# Import libraries
import glob
import numpy
import os
import os.path
import sys

# Constant
VECTOR_SIZE = 10

# Main method
def main():
    # Retrieve user arguments 
    # provided to the Python program
    args = sys.argv[1:]

    # if args are empty
    if len(args) < 2:
        # show instruction
        print("usage: directory-name num-of-clusters")
        sys.exit(1)

    # if args is a list of 2 items
    # check first item
    # get the full directory path
    dir_path = os.path.join(os.getcwd(), args[0])
    if not os.path.isdir(dir_path):
        # show instruction
        print("usage: directory-name num-of-clusters")
        print("warning: provide valid directory name")
        sys.exit(1)

    # check second item
    if not args[1].isdecimal():
        # show instruction
        print("usage: directory-name num-of-clusters")
        print("warning: provide an integer in the set of natural number")
        sys.exit(1)
    
    # get the number of clusters specified on terminal
    num_clusters = int(args[1])
    
    # get a list of files from directory
    file_list = glob.glob(dir_path+"/*.txt")
    
    # file 1
    file1 = file_list[0]

    doc = {}

    with open(file1) as rFile:
        for line in rFile:
            words = line.split()
            for pos in range(len(words)):
                w = words[pos]
                if w == "_": continue
                if not doc.get(w, None):
                    # vector for word 3
                    doc[w] = [0]*VECTOR_SIZE
                    # word 1
                    doc[w][hash_fn_1(words[pos-2]+"-2")] = hash_fn_2(words[pos-2]+"-2") 
                    # word 2
                    doc[w][hash_fn_1(words[pos-1]+"-1")] = hash_fn_2(words[pos-1]+"-1")
                    # word 4
                    doc[w][hash_fn_1(words[pos+1]+"+1")] = hash_fn_2(words[pos-2]+"+1")
                    # word 5
                    doc[w][hash_fn_1(words[pos+2]+"+2")] = hash_fn_2(words[pos+2]+"+2") 
                else:
                    doc[w][hash_fn_1(words[pos-2]+"-2")] = hash_fn_2(words[pos-2]+"-2") 
                    # word 2
                    doc[w][hash_fn_1(words[pos-1]+"-1")] = hash_fn_2(words[pos-1]+"-1")
                    # word 4
                    doc[w][hash_fn_1(words[pos+1]+"+1")] = hash_fn_2(words[pos-2]+"+1")
                    # word 5
                    doc[w][hash_fn_1(words[pos+2]+"+2")] = hash_fn_2(words[pos+2]+"+2") 

    
    # Testing
    print("Document: ", file1)
    print("Document dictionary: ", doc)


def hash_fn_1(word):
    """This hash function maps
       a string to a number
       between 0 and 9.
    """
    # keep the total value
    # after adding values
    # represented by each character
    total = 0

    for pos in range(len(word)):
        # add value for each character 
        # multiplied by their position 
        # in the string
        total += (ord(word[pos]) * (pos + 1))

    return total % VECTOR_SIZE

def hash_fn_2(word):
    """This hash function
       maps a string to 
       plus or minus one.
    """
    str_value = 0

    for pos in range(len(word)):
        str_value += (ord(word[pos]) * (pos + 1))

    if str_value % 2:
        return 1

    return -1

# Execute script
if __name__ == "__main__":
	main()