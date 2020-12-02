from day_1 import compute_product, read_number_list


def test_read_number_list():
    """Check numbers are read from file to a list"""
    input_file = "test_data_input.txt"
    assert read_number_list(input_file) == [1721, 979, 366, 299, 675, 1456]


def test_compute_product():
    """Test compute_product()"""
    assert compute_product(read_number_list("data_input.txt"), 2) == 913824
