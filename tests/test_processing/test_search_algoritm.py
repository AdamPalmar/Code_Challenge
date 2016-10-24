from hasher import md5_hasher
from processing import search_algoritms as s_a
from solvers import anagram_solver


def test_check_three_tuples():
    tuple1 = ("This", None)
    tuple2 = ("is", None)
    tuple3 = ("Sparta!", None)

    sentence = "This is Sparta!"
    hashed_sentence = md5_hasher.md5_hash_sentence(sentence)

    hashed_result = s_a.check_three_tuples(tuple1,
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

    result_sentence = s_a.search_for_combination(anagram_product_sum,
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

    result_sentence = s_a.search_for_combination(anagram_product_sum,
                                                 list_tuple_prime_sums,
                                                 md5_hash_sentence)

    invalid_sentence = sentence_to_find + "not valid anymore"

    assert result_sentence != invalid_sentence


def test_search_multi_core_binary_search_numpy():
    solver = anagram_solver.MultipleCpuSolverBinaryNumpySearch()

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

    result = solver.distribute_work(list_tuple_prime_sums,
                                    anagram_product_sum,
                                    md5_hash_sentence)

    assert result == sentence_to_find