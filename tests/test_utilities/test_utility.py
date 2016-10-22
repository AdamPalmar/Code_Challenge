from utilities import utility

# py.test --cov=test_utility.py --cov=utilities
#  --cov-report=term --pep8 --flakes --mccabe -v


def test_remove_space_from_sentence():
    sentence = "hello test world"
    expected = "hellotestworld"
    result = utility.remove_space_from_sentence(sentence)
    assert expected == result


def test_sort_dict():
    a, b, c = 2, 3, 5

    dict_prime_sums = {"abc": a * b * c,
                       "ab": a * b,
                       "ac": a * c,
                       "a": a,
                       "b": b}

    sorted_list_of_tuple = [("a", a), ("b", b),
                            ("ab", a * b), ("ac", a * c),
                            ("abc", a * b * c)]

    result = utility.get_sorted_list_of_tuple_from_dict(dict_prime_sums)

    assert result == sorted_list_of_tuple


def test_remove_empty_strings():
    list_of_words = [" ", "", "test'", "valid_string"]
    expected = ["test'", "valid_string"]
    result = utility.remove_empty_space_in_list(list_of_words)

    assert result == expected
