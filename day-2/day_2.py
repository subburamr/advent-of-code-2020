"""Day 2 solution"""
from collections import Counter


def calculate_invalid_passwords(input_file):
    password_text = open(input_file).readlines()
    num_valid_passwords = 0
    for line in password_text:
        policy, password = line.split(": ")
        min_max, alphabet = policy.split()
        a_min, a_max = min_max.split("-")
        counter = Counter(password)
        if int(a_min) <= counter[alphabet] <= int(a_max):
            num_valid_passwords += 1
    return num_valid_passwords


def calculate_invalid_position(input_file):
    password_text = open(input_file).readlines()
    num_valid_passwords = 0
    for line in password_text:
        policy, password = line.split(": ")
        positions, alphabet = policy.split()
        pos_1, pos_2 = positions.split("-")
        pass_list = list(password)
        if bool(pass_list[int(pos_1) - 1] == alphabet) != bool(
            pass_list[int(pos_2) - 1] == alphabet
        ):
            num_valid_passwords += 1
    return num_valid_passwords


if __name__ == "__main__":
    print(calculate_invalid_passwords("data_input.txt"))
    print(calculate_invalid_position("data_input.txt"))
