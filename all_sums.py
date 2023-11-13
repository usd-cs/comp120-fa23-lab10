from sys import argv
from typing import Optional

def all_sums(values: list[int], sum_so_far: int = 0) -> None:
   """Prints out the sum of all possible subsets of the given values, assume
   we have already made choices to have given us the sum of <total>."""

   pass  # replace this with your implementation

if __name__ == "__main__":
    if len(argv) < 2:
        print("Incorrect number of arguments")
    else:
        int_list = [int(n) for n in argv[1:]]
        all_sum(int_list)
