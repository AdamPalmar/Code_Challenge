from solvers import anagram_solver
from hasher import md5_hasher
import os


def test_multiple_cpu_solver_binary_numpy_search_three_words():
    solver = anagram_solver.MultipleCpuSolverBinaryNumpySearch()

    sentence_to_find = "zen above actor"
    md5_hash = md5_hasher.md5_hash_sentence(sentence_to_find)

    anagram_given = "nezabvoe torca"

    # todo: i don't like this reference to path!

    path_to_file = os.path.abspath("test_wordlist")

    result_sentece = solver.solve_anagram(anagram_sentence=anagram_given,
                                          path_to_wordlist=path_to_file,
                                          md5_hash=md5_hash)

    assert result_sentece == sentence_to_find


def test_multiple_cpu_solver_binary_numpy_search_two_words():
    solver = anagram_solver.MultipleCpuSolverBinaryNumpySearch()

    sentence_to_find = "zen actor"
    md5_hash = md5_hasher.md5_hash_sentence(sentence_to_find)

    anagram_given = "nezt orca"

    # todo: i don't like this reference to path!

    path_to_file = os.path.abspath("test_wordlist")

    result_sentece = solver.solve_anagram(anagram_sentence=anagram_given,
                                          path_to_wordlist=path_to_file,
                                          md5_hash=md5_hash)

    assert result_sentece == sentence_to_find


def test_multiple_cpu_solver_binary_numpy_search_one_word():
    solver = anagram_solver.MultipleCpuSolverBinaryNumpySearch()

    sentence_to_find = "zen"
    md5_hash = md5_hasher.md5_hash_sentence(sentence_to_find)

    anagram_given = "ezn"

    # todo: i don't like this reference to path!

    path_to_file = os.path.abspath("test_wordlist")

    result_sentence = solver.solve_anagram(anagram_sentence=anagram_given,
                                           path_to_wordlist=path_to_file,
                                           md5_hash=md5_hash)

    assert result_sentence == sentence_to_find


def test_main():
    anagram_sentence = "poultry outwits ants"
    path_to_wordlist = "test_wordlist"
    result = anagram_solver.main(anagram_sentence, path_to_wordlist)
    expected_result = "pastils turnout towy"

    assert result == expected_result


def test_did_not_find_anagram_sentence():
    solver = anagram_solver.MultipleCpuSolverBinaryNumpySearch()

    sentence_to_find = "aaa bbb ccc"
    md5_hash = md5_hasher.md5_hash_sentence(sentence_to_find)

    anagram_given = "ezn"

    # todo: i don't like this reference to path!

    path_to_file = os.path.abspath("test_wordlist")

    result_sentence = solver.solve_anagram(anagram_sentence=anagram_given,
                                           path_to_wordlist=path_to_file,
                                           md5_hash=md5_hash)

    expected_result = "No result"

    assert result_sentence == expected_result
