from processing import binary_search as search
from processing import numpy_processing as npp
import numpy as np


def test_binary_search_of_array():
    numpy_array = np.array([2, 3, 5, 7, 11])
    expected_index_of_values = [0, 1, 2, 3, 4]
    look_for_values = [2, 3, 5, 7, 11]
    list_of_results = list()

    for num in look_for_values:
        index_of_value = search.search_array(numpy_array, num)
        list_of_results.append(index_of_value)
    print("Result ", list_of_results)
    assert list_of_results == expected_index_of_values


def test_binary_search_not_in_array():
    numpy_array = np.array([2, 3, 5, 7, 11])
    expected_index_of_values = [-1, -1, -1, -1]
    look_for_values = [-1, 1, 4, 100]
    list_of_results = list()
    for num in look_for_values:
        index_of_value = search.search_array(numpy_array, num)
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
        index_of_value = search.search_list_tuple(list_of_tuple, num)
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
        index_of_value = search.search_list_tuple(list_of_tuple, num)
        list_of_results.append(index_of_value)

    assert list_of_results == expected_index_of_values


def test_get_list_of_neighbors_from_array_top_case():
    a, b, c = 2, 3, 5

    aba = a * b * a
    aab = a * a * b
    baa = b * a * a
    abc = a * b * c

    list_of_tuple = [("aba", aba),
                     ("aab", aab),
                     ("baa", baa),
                     ("abc", abc)]

    array_of_words = npp.convert_list_tuple_into_numpy_array(list_of_tuple)

    (array_prime_sums,
     top_ref_array,
     bot_ref_array) = npp.get_prime_product_of_arrays(4, array_of_words)

    permutation = array_prime_sums.argsort()

    array_prime_sums = array_prime_sums[permutation]
    top_ref_array = top_ref_array[permutation]
    bot_ref_array = bot_ref_array[permutation]

    print("array of words", array_of_words)
    print("array of prime sums", array_prime_sums)

    index = search.search_array(array_prime_sums, aba * aab)

    print(top_ref_array[1])
    neighbors_list = search.get_list_same_products_from_array(list_of_tuple,
                                                              array_prime_sums,
                                                              top_ref_array,
                                                              bot_ref_array,
                                                              index)

    expected_result = [("aab", "baa"), ("aba", "baa"), ("aba", "aab")]

    assert expected_result == neighbors_list


def test_get_list_of_neighbors_from_array_bottom_case():
    pass

    # Todo: add test where all are neighbors
