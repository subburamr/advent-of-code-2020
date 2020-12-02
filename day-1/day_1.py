### Return two numbers whose sum is 2020 and return their multiplication
import itertools
import operator
from functools import reduce


def compute_product(number_list, num_summands):
    iter = itertools.combinations(number_list, num_summands)
    for it in iter:
        if sum(it) == 2020:
            return reduce(operator.mul, it, 1)


def read_number_list(input_file):
    content = open(input_file).readlines()
    return [int(num) for num in content]


if __name__ == "__main__":
    read_number_list("data_input.txt")
    print(compute_product(read_number_list("data_input.txt"), 2))
    print(compute_product(read_number_list("data_input.txt"), 3))
