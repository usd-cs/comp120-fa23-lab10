from sys import argv
from time import time
from typing import Optional
import json

def find_word(possible: str, prefix: str, lex: dict) -> Optional[str]:
    """Returns a word (among those listed in the <lex> dictionary) that is a
    permutation of the <possible> characters, with <prefix> being placed at
    the beginning of each permutation."""

    if len(possible) == 0:
        if prefix in lex:
            return prefix
        else:
            return None
    else:
        for i in range(len(possible)):
            remaining = possible[0:i] + possible[i+1:]

            # try finding a word with starts with prefix + the first possible
            # character.
            word = find_word(remaining, prefix + possible[i], lex)

            # see if we found it!
            if word is not None:
                return word

        return None # went through all possibilites and didn't find a word


if __name__ == "__main__":
    if len(argv) != 2:
        print("Incorrect number of arguments")
    else:

        with open("english_dictionary.json") as english_file:
            english = json.load(english_file)

        start = time()
        word = find_word(argv[1], '', english)
        end = time()
        diff = end - start

        if word:
            print("Found word:", word)
        else:
            print("No word found!")

        print(f"Time elapsed: {diff:.7f}")
