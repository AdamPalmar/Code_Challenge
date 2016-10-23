from processing import binary_search
import numpy as np


def test_binary_search_of_array():
    numpy_array = np.array([2, 3, 5, 7, 11])
    expected_index_of_values = [0, 1, 2, 3, 4]
    look_for_values = [2, 3, 5, 7, 11]
    list_of_results = list()

    for num in look_for_values:
        index_of_value = binary_search.search_array(numpy_array, num)
        list_of_results.append(index_of_value)
    print("Result ", list_of_results)
    assert list_of_results == expected_index_of_values


def test_binary_search_not_in_array():
    numpy_array = np.array([2, 3, 5, 7, 11])
    expected_index_of_values = [-1, -1, -1, -1]
    look_for_values = [-1, 1, 4, 100]
    list_of_results = list()
    for num in look_for_values:
        index_of_value = binary_search.search_array(numpy_array, num)
        list_of_results.append(index_of_value)

    assert list_of_results == expected_index_of_values


def test_binary_search_of_list_of_tuple():
    list_of_tuple = [("a", 2),
                     ("b", 3),
                     ("c", 5),
                     ("d", 7),
                     ("e", 11)]

    expected_index_of_values = [0, 1, 2, 3, 4]
    look_for_values = [2, 3, 5, 7, 11]
    list_of_results = list()

    for num in look_for_values:
        index_of_value = binary_search.search_list_tuple(list_of_tuple, num)
        list_of_results.append(index_of_value)

    assert list_of_results == expected_index_of_values


def test_binary_search_not_in_list_of_tuple():
    list_of_tuple = [("a", 2),
                     ("b", 3),
                     ("c", 5),
                     ("d", 7),
                     ("e", 11)]

    expected_index_of_values = [-1, -1, -1, -1, -1]
    look_for_values = [-1, 0, 1, 4, 100]
    list_of_results = list()

    for num in look_for_values:
        index_of_value = binary_search.search_list_tuple(list_of_tuple, num)
        list_of_results.append(index_of_value)

    assert list_of_results == expected_index_of_values


def test_get_list_of_neighbors_from_array_top_case():
    a, b, c, d, e = 2, 3, 5, 7, 11
    list_tuple_word_prime = [("a", a),
                             ("b", b),
                             ("c", c),
                             ("d", d),
                             ("e", e),
                             ("ae", a * e),
                             ("ea", e * a)]

    array_prime_sums = np.array([a, b, c, d, e, a * e, e * a])

    index = binary_search.search_array(array_prime_sums=array_prime_sums,
                                       value_to_find=a * e)

    neighbors = binary_search.get_list_of_same_neighbors_for_array(list_tuple_word_prime=list_tuple_word_prime,
                                                                   array_of_prime_sums=array_prime_sums,
                                                                   index=index)
    expected_result = ["ae", "ea"]

    word_found = list_tuple_word_prime[index][0]

    neighbors.append(word_found)

    assert expected_result == neighbors


def test_get_list_of_neighbors_from_array_bottom_case():
    pass

    # Todo: add test where all are neighbors
