from sys import argv
from time import time

def subsets(possible: str, prefix: str = '') -> None:
    """ Prints all subsets of the <possible> characters, with <prefix>
    being placed at the beginning of each subset."""

    if len(possible) == 0:
        print(prefix)
    else:
        subsets(possible[1:], prefix + possible[0]); # include first char
        subsets(possible[1:], prefix) # exclude first char

if __name__ == "__main__":
    if len(argv) != 2:
        print("Incorrect number of arguments")
    else:
        start = time()
        subsets(argv[1])
        end = time()
        diff = end - start
        print(f"Time elapsed: {diff:.7f}")
