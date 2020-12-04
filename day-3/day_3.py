"""Day 3 solution."""
from collections import defaultdict
from typing import DefaultDict


def load_map(input_file):
    """Read a file line by line and store it in dict.

    Parameters
    ----------
    input_file : str
        input file containing map

    Returns
    -------
    DefaultDict[Dict]
        Dict representation
    """
    with open(input_file) as f:
        map_lines = f.read().splitlines()
    map_dict = defaultdict(dict)
    for line_num, line_content in enumerate(map_lines):
        map_dict[line_num] = {
            char_idx: char for char_idx, char in enumerate(line_content)
        }
    return map_dict


def calculate_num_trees(input_file, right, down):
    """Calculate number of trees on the path.

    Parameters
    ----------
    input_file : str
        input file containing the map representation.
    """
    map_dict = load_map(input_file)
    num_trees = 0
    curr_row_pos = 0
    num_rows = len(map_dict[0])
    for i in range(0, len(map_dict), down):
        if (i + down) < len(map_dict):
            val = map_dict[i + down]
            curr_row_pos = curr_row_pos + right
            curr_idx = curr_row_pos % num_rows
            if val[curr_idx] == "#":
                num_trees += 1
    return num_trees


if __name__ == "__main__":
    tuple_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    prod = 1
    for right_down in tuple_list:
        prod = prod * calculate_num_trees("data_input.txt", *right_down)
