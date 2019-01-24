#!/usr/bin/python3


__author__ = "Kevin GUILLEMOT"
__credits__ = []
__license__ = "Apache2.0"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "kevin.guillemot2@gmail.com"
__doc__ = "Create a pattern for fuzzing"



import sys



def create_pattern(nb_bytes):
    alphabet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "abcdefghijklmnopqrstuvwxyz",
                "123456789"]

    result = ""
    cpt = 0
    cpt2 = 0

    while len(result) < nb_bytes:
        result += alphabet[cpt%3][int(cpt/3)%len(alphabet[cpt%3])]
        cpt += 1

    return result





if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage : {} <nb_bytes>".format(sys.argv[0]))
        sys.exit(0)

    """ Convert argv[1] to int """ 
    try:
        nb_bytes = int(sys.argv[1])
    except ValueError:
        print("ERROR: Argument 1 must be an int.")
        sys.exit(1)

    pattern = create_pattern(nb_bytes)

    print(pattern)
