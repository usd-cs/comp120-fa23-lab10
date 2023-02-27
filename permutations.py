from sys import argv
from typing import Optional

def permute(possible: str, prefix: str = '') -> None:
    """ Prints all permutations of the <possible> characters, with <prefix>
    being placed at the beginning of each permutation."""
    if len(possible) == 0:
        print(prefix)
    else:
        for i in range(len(possible)):
            remaining = possible[0:i] + possible[i+1:]
            permute(remaining, prefix + possible[i])


if __name__ == "__main__":
    if len(argv) != 2:
        print("Incorrect number of arguments")
    else:
        permute(argv[1])
