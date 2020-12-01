### Return two numbers whose sum is 2020 and return their multiplication
import itertools
import operator
from functools import reduce


def compute_day_1_two_numbers(input_file):
    content = open(input_file).readlines()
    numbers = [int(num) for num in content]
    sorted_numbers = sorted(numbers)
    for num in sorted_numbers:
        if (2020 - num) in sorted_numbers:
            return num * ((2020 - num))


def compute_day_1_three_numbers(input_file):
    content = open(input_file).readlines()
    numbers = [int(num) for num in content]
    iter = itertools.combinations(numbers, 3)
    for it in iter:
        if sum(it) == 2020:
            return reduce(operator.mul, it, 1)


print(compute_day_1_two_numbers("data_input.txt"))
print(compute_day_1_three_numbers("data_input.txt"))
