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

    result_sentece = solver.solve_anagram(anagram_sentence=anagram_given,
                                          path_to_wordlist=path_to_file,
                                          md5_hash=md5_hash)

    assert result_sentece == sentence_to_find
