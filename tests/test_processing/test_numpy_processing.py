from processing import numpy_processing


def test_get_correct_words_from_list_with_array_ref():
    expected_word_1 = "a"
    expected_word_2 = "c"

    list_of_tuple = [("a", 2), ("b", 3), ("c", 5), ("d", 7), ("e", 11)]
    test_converted_array = numpy_processing.convert_list_tuple_into_numpy_array(list_of_tuple)

    num_words = len(list_of_tuple)

    result, top_ref, bot_ref = numpy_processing.get_prime_product_of_arrays(num_words, test_converted_array)

    index_to_look_at = 1
    word_1, word_2 = numpy_processing.get_words_from_list_from_arrays(list_of_tuple=list_of_tuple,
                                                                      top_ref_array=top_ref,
                                                                      bottom_ref_array=bot_ref,
                                                                      index=index_to_look_at)
    # top_array [a a a a b b b c c d]
    # bot_array [b c d e c d e d e e]

    # index_ref [0 1 2 3 4 5 6 7 8 9]

    assert expected_word_1 == word_1
    assert expected_word_2 == word_2
