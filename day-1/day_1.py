"""Day 1  Solution"""
import itertools
import operator
from functools import reduce
from typing import List


def compute_product(number_list: List[int], num_summands: int) -> int:
    """Get the numbers which sum to 2020 and return their product

    Parameters
    ----------
    number_list : List
        List of numbers read from the input
    num_summands : int
        Number of summands - 2 or 3

    Returns
    -------
    int
        The product of the numbers
    """
    iter = itertools.combinations(number_list, num_summands)
    for it in iter:
        if sum(it) == 2020:
            return reduce(operator.mul, it, 1)


def read_number_list(input_file: str) -> List[int]:
    """Read a file of numbers and load the contents in a list

    Parameters
    ----------
    input_file : str
        input file

    Returns
    -------
    List
        List of integers
    """
    content = open(input_file).readlines()
    return [int(num) for num in content]


if __name__ == "__main__":
    read_number_list("data_input.txt")
    print(compute_product(read_number_list("data_input.txt"), 2))
    print(compute_product(read_number_list("data_input.txt"), 3))
