from preproccessing import word_prime_converter as wpc
import os


# py.test --cov=test_word_prime_converter.py
# --cov=preproccessing --cov-report=term --pep8 --flakes --mccabe


def test_dict_words_to_prime_product_sums():
    list_of_words = ["abc", "ab", "a"]
    a, b, c = 2, 3, 5
    dict_char_to_prime = {"a": 2,
                          "b": 3,
                          "c": 5}
    expected_result = {"abc": a * b * c,
                       "ab": a * b,
                       "a": a}
    result = wpc.dict_words_to_prime_product_sums(list_of_words,
                                                  dict_char_to_prime)
    assert expected_result == result


def test_prime_product_sum_of_anagram_sentence():
    anagram_sentence = "abc ab ac c"
    a, b, c = 2, 3, 5
    dict_char_to_prime = {"a": 2,
                          "b": 3,
                          "c": 5}
    expected_result = a * b * c * a * b * a * c * c
    result = wpc.prime_product_sum_of_anagram_sentence(anagram_sentence,
                                                       dict_char_to_prime)
    assert expected_result == result


def test_dict_prime_numbers_to_anagram_character():
    anagram_sentence = "abc ab c"
    a, b, c = 2, 3, 5
    expected_dict = {"a": a,
                     "b": b,
                     "c": c}

    result = wpc.dict_prime_numbers_to_anagram_character(anagram_sentence)

    assert expected_dict == result


def test_get_sorted_dict_char_to_prime():
    # Todo: Fix reference to file.
    # Currently based on where the test is called from. No good.
    path_to_file = str(os.getcwd()) + "/test_preproccessing/file_char_to_prime"

    anagram_sentence = "abc ab c"

    a, b, c = 2, 3, 5
    expected_dict = [("a", a),
                     ("b", b),
                     ("c", c),
                     ("ab", a * b),
                     ("ac", a * c),
                     ("abc", a * b * c)]

    result_dict = wpc.get_sorted_list_tuple_char_to_prime(path_to_file,
                                                          anagram_sentence)
    assert result_dict == expected_dict


def test_get_product_sum_anagram_sentence():
    anagram_sentence = "abc def ab ac de df a b c d e f"
    a, b, c, d, e, f = 2, 3, 5, 7, 11, 13

    _abc = a * b * c
    _def = d * e * f
    _ab = a * b
    _ac = a * c
    _de = d * e
    _df = d * f
    _abcdef = a * b * c * d * e * f

    expected_product_sum = _abc * _def * _ab * _ac * _de * _df * _abcdef

    result_sum = wpc.get_product_sum_anagram_sentence(anagram_sentence)

    assert result_sum == expected_product_sum
