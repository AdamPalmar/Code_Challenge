from md5_hashing import md5_hasher
from fileIO import file_writer
from processing import binary_search, numpy_processing
from preproccessing import wordlist_cleaner as wlc
from profiler import line_profiling
import numpy as np
import time


def check_three_tuples(tuple1, tuple2, tuple3, md5_hash="4624d200580677270a54ccff86b9610e"):
    tuple_hash = md5_hasher.md5_hash_sentence(tuple1[0] + " " + tuple2[0] + " " + tuple3[0])

    if tuple_hash == md5_hash:
        print("-------Found the hash------- ", tuple1, tuple2, tuple3)
        return True
    else:
        return False


def check_three_words(word_one, word_two, word_three, md5_hash="4624d200580677270a54ccff86b9610e"):
    word_hash = md5_hasher.md5_hash_sentence(word_one + " " + word_two + " " + word_three)

    if word_hash == md5_hash:
        return True
    else:
        return False


# Todo: Make search run more then three loops
# Todo: Add early stop in for loops
# Todo: Is it a list of tuples though?
def search_for_combination(anagram_product_sum, list_tuple_word_prime, md5_hash="4624d200580677270a54ccff86b9610e"):
    # print(anagram_product_sum)
    for tuple1 in list_tuple_word_prime:
        for tuple2 in list_tuple_word_prime:
            for tuple3 in list_tuple_word_prime:
                product_sum = tuple1[1] * tuple2[1] * tuple3[1]

                if product_sum == anagram_product_sum:
                    # print(tuple1, tuple2, tuple3)
                    result = check_three_tuples(tuple1, tuple2, tuple3, md5_hash)
                    if result:
                        result_sentence = str(tuple1[0] + " " + tuple2[0] + " " + tuple3[0])
                        file_writer.write_solution_into_file(result_sentence,
                                                             "../solution")
                        return result_sentence


def search_for_combination_binary_search(anagram_product_sum, list_tuple_word_prime,
                                         md5_hash="4624d200580677270a54ccff86b9610e"):
    for tuple1 in list_tuple_word_prime:
        for tuple2 in list_tuple_word_prime:

            last_prime_value_needed = anagram_product_sum / (tuple1[1] * tuple2[1])
            # Todo: fix the amount of ifs!

            if last_prime_value_needed.is_integer():
                index = binary_search.search_list_tuple(list_tuple_word_prime, int(last_prime_value_needed))
                if index != -1:
                    tuple3 = list_tuple_word_prime[index]
                    product_sum = tuple1[1] * tuple2[1] * tuple3[1]

                    if product_sum == anagram_product_sum:
                        # print(tuple1, tuple2, tuple3)
                        result = check_three_tuples(tuple1, tuple2, tuple3, md5_hash)

                        if result:
                            result_sentence = str(tuple1[0] + " " + tuple2[0] + " " + tuple3[0])
                            file_writer.write_solution_into_file(result_sentence,
                                                                 "../solution")

                            return result_sentence


def search_multi_core_binary_search(anagram_product_sum,
                                    list_tuple_word_prime,
                                    chunk_index_start,
                                    chunk_index_stop,
                                    result_shared_mem_ref,
                                    md5_hash="4624d200580677270a54ccff86b9610e"):
    for tuple1 in list_tuple_word_prime[chunk_index_start: chunk_index_stop]:

        for tuple2 in list_tuple_word_prime:

            last_prime_value_needed = anagram_product_sum / (tuple1[1] * tuple2[1])
            # Todo: fix the amount of ifs!

            if last_prime_value_needed.is_integer():
                index = binary_search.search_list_tuple(list_tuple_word_prime,
                                                        int(last_prime_value_needed))
                if index != -1:
                    tuple3 = list_tuple_word_prime[index]
                    product_sum = tuple1[1] * tuple2[1] * tuple3[1]

                    if product_sum == anagram_product_sum:
                        # print(tuple1, tuple2, tuple3)

                        result = check_three_tuples(tuple1, tuple2, tuple3, md5_hash)

                        if result:
                            result_sentence = str(tuple1[0] + " " + tuple2[0] + " " + tuple3[0])
                            file_writer.write_solution_into_file(result_sentence,
                                                                 "../solution")

                            result_shared_mem_ref.value = result_sentence
                            return result_sentence


# @line_profiling.profile(follow=[])
def search_multi_core_binary_search_numpy(anagram_product_sum,
                                          list_tuple_word_prime,
                                          chunk_index_start,
                                          chunk_index_stop,
                                          result_shared_mem_ref,
                                          md5_hash="4624d200580677270a54ccff86b9610e"):
    array_of_word_values = numpy_processing.convert_list_tuple_into_numpy_array(list_tuple_word_prime)

    num_words = len(array_of_word_values)

    (product_array,
     top_ref_word,
     bot_ref_word) = numpy_processing.get_prime_product_of_arrays(num_words, array_of_word_values)

    for index, product_sum in enumerate(array_of_word_values[chunk_index_start: chunk_index_stop]):

        prime_product_needed = anagram_product_sum / product_sum

        if prime_product_needed.is_integer():

            index_of_product_array = binary_search.search_array(product_array, int(prime_product_needed))

            if index_of_product_array != -1:
                word_one = numpy_processing.get_word_from_list_in_array(list_tuple_word_prime, index, chunk_index_start)

                list_of_candidate_words = binary_search.get_list_same_products_from_array(list_tuple_word_prime,
                                                                                          product_array,
                                                                                          top_ref_word,
                                                                                          bot_ref_word,
                                                                                          index_of_product_array)

                check_combinations(word_one, list_of_candidate_words, md5_hash, result_shared_mem_ref)


def search_all_combinations():
    pass


def check_combinations(word_one, list_of_candidates, md5_hash, result_shared_mem_ref):
    for candidates in list_of_candidates:

        word_two = candidates[0]
        word_three = candidates[1]

        result_one_two_three = check_three_words(word_one, word_two, word_three, md5_hash)
        result_one_three_two = check_three_words(word_one, word_three, word_two, md5_hash)
        if result_one_two_three:
            sentence = word_one + " " + word_two + " " + word_three
            save_solution(sentence)
            result_shared_mem_ref.value = sentence
        elif result_one_three_two:
            sentence = word_one + " " + word_three + " " + word_two
            save_solution(sentence)
            result_shared_mem_ref.value = sentence


def save_solution(sentence):
    print("--------Found the hash------", sentence)
    file_writer.write_solution_into_file(sentence, "../solution")
