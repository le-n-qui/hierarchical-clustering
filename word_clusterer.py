# Word Clusterer

# Import libraries
import glob
import os
import os.path
import sys

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

# Execute script
if __name__ == "__main__":
	main()