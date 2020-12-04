from day_3 import calculate_num_trees


def test_calculate_num_trees():
    assert calculate_num_trees("test_data_input.txt", 1, 1) == 2
    assert calculate_num_trees("test_data_input.txt", 3, 1) == 7
    assert calculate_num_trees("test_data_input.txt", 5, 1) == 3
    assert calculate_num_trees("test_data_input.txt", 7, 1) == 4
    assert calculate_num_trees("test_data_input.txt", 1, 2) == 2
