from day_1 import compute_day_1_three_numbers, compute_day_1_two_numbers


def test_compute_day_1_two_numbers():
    input_file = "test_data_input.txt"
    assert compute_day_1_two_numbers(input_file) == 514579


def test_compute_day_1_three_numbers():
    input_file = "test_data_input.txt"
    assert compute_day_1_three_numbers(input_file) == 241861950
