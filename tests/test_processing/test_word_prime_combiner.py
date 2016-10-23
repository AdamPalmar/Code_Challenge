from md5_hashing import md5_hasher
from processing import search_algoritms as wp_combiner


def test_check_three_tuples():
    tuple1 = ("This", None)
    tuple2 = ("is", None)
    tuple3 = ("Sparta!", None)

    sentence = "This is Sparta!"
    hashed_sentence = md5_hasher.md5_hash_sentence(sentence)

    hashed_result = wp_combiner.check_three_tuples(tuple1,
                                                   tuple2,
                                                   tuple3,
                                                   hashed_sentence)

    assert hashed_result


def test_search_for_combination():
    sentence_to_find = "abc ab ac"

    md5_hash_sentence = md5_hasher.md5_hash_sentence(sentence_to_find)

    a, b, c = 2, 3, 5

    anagram_product_sum = a * b * c * a * b * a * c

    list_tuple_prime_sums = [("abc", a * b * c),
                             ("cba", c * b * a),
                             ("ab", a * b),
                             ("ac", a * c),
                             ("ba", b * a),
                             ("bc", b * c),
                             ("a", a),
                             ("b", b),
                             ("c", c)]

    result_sentence = wp_combiner.search_for_combination(anagram_product_sum,
                                                         list_tuple_prime_sums,
                                                         md5_hash_sentence)

    assert result_sentence == sentence_to_find


def test_search_for_combination_check_invalid_result():
    sentence_to_find = "abc ab ac"

    md5_hash_sentence = md5_hasher.md5_hash_sentence(sentence_to_find)

    a, b, c = 2, 3, 5

    anagram_product_sum = a * b * c * a * b * a * c

    list_tuple_prime_sums = [("abc", a * b * c),
                             ("cba", c * b * a),
                             ("ab", a * b),
                             ("ac", a * c),
                             ("ba", b * a),
                             ("bc", b * c),
                             ("a", a),
                             ("b", b),
                             ("c", c)]

    result_sentence = wp_combiner.search_for_combination(anagram_product_sum,
                                                         list_tuple_prime_sums,
                                                         md5_hash_sentence)

    invalid_sentence = sentence_to_find + "not valid anymore"

    assert result_sentence != invalid_sentence
