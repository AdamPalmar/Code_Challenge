from processing import numpy_processing as np


def test_get_correct_words_from_list_with_array_ref():
    expected_word_1 = "a"
    expected_word_2 = "c"

    list_of_tuple = [("a", 2), ("b", 3), ("c", 5), ("d", 7), ("e", 11)]
    converted_array = np.convert_list_tuple_into_numpy_array(list_of_tuple)

    num_words = len(list_of_tuple)

    result, top_ref, bot_ref = np.get_prime_product_of_arrays(num_words,
                                                              converted_array)

    index = 1
    word_1, word_2 = np.get_words_from_list_in_arrays(list_of_tuple,
                                                      top_ref,
                                                      bot_ref,
                                                      index)
    # top_array [a a a a b b b c c d]
    # bot_array [b c d e c d e d e e]

    # index_ref [0 1 2 3 4 5 6 7 8 9]

    assert expected_word_1 == word_1
    assert expected_word_2 == word_2
