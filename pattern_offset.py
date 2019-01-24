#!/usr/bin/python3


__author__ = "Kevin GUILLEMOT"
__credits__ = []
__license__ = "Apache2.0"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "kevin.guillemot2@gmail.com"
__doc__ = "Get the number of bytes between a given pattern and the generated pattern"



import sys



def pattern_offset(nb_bytes, pattern):
    alphabet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "abcdefghijklmnopqrstuvwxyz",
                "123456789"]

    result = ""
    cpt = 0
    cpt2 = 0

    while len(result) < nb_bytes:
        result += alphabet[cpt%3][int(cpt/3)%len(alphabet[cpt%3])]
        cpt += 1
        if len(result) >= len(pattern) and result[-len(pattern):] == pattern:
            return cpt-len(pattern)

    return "No match"


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage : {} <nb_bytes> <addr>".format(sys.argv[0]))
        sys.exit(0)

    """ Convert argv[1] to int """ 
    try:
        nb_bytes = int(sys.argv[1])
    except ValueError:
        print("ERROR: Argument 1 must be an int.")
        sys.exit(1)


    pattern = ""
    if sys.argv[2][:2].lower() == "0x":
        cpt = len(sys.argv[2])
        while cpt-2 >= 2:
            pattern += chr(int("0x"+sys.argv[2][cpt-2:cpt], 16))
            cpt -= 2
    else:
        pattern = sys.argv[2]

    res = pattern_offset(nb_bytes, pattern)

    print("Offset = ",res)
