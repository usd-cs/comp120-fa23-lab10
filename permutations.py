from sys import argv
from typing import Optional

def word_scramble(options: str, so_far: str = '') -> None:
    """ Prints all permutations of the <options> characters, with <so_far>
    being placed at the beginning of each permutation."""
    if len(options) == 0:
        print(so_far)
    else:
        for i in range(len(options)):
            # choose an option...
            choice = options[i]
            remaining = options[0:i] + options[i+1:]

            # explore that choice recursively
            word_scramble(remaining, so_far + choice)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Incorrect number of arguments")
    else:
        word_scramble(argv[1], "")
