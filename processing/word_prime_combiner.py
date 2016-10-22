from md5_hashing import md5_hasher
from fileIO import file_writer
from processing import binary_search
from preproccessing import wordlist_cleaner as wlc

import time


def check_three_tuples(tuple1, tuple2, tuple3, md5_hash="4624d200580677270a54ccff86b9610e"):
    tuple_hash = md5_hasher.md5_hash_sentence(tuple1[0] + " " + tuple2[0] + " " + tuple3[0])

    if tuple_hash == md5_hash:
        print("-------Found the hash------- ", tuple1, tuple2, tuple3)
        return True
    else:
        return False


# Todo: Make search run more then three loops
# Todo: Add early stop in for loops
# Todo: Is it a list of tuples though?
def search_for_combination(anagram_product_sum, list_tuple_prime_sums, md5_hash="4624d200580677270a54ccff86b9610e"):
    # print(anagram_product_sum)
    for tuple1 in list_tuple_prime_sums:
        for tuple2 in list_tuple_prime_sums:
            for tuple3 in list_tuple_prime_sums:
                product_sum = tuple1[1] * tuple2[1] * tuple3[1]

                if product_sum == anagram_product_sum:
                    # print(tuple1, tuple2, tuple3)
                    result = check_three_tuples(tuple1, tuple2, tuple3, md5_hash)
                    if result:
                        result_sentence = str(tuple1[0] + " " + tuple2[0] + " " + tuple3[0])
                        file_writer.write_solution_into_file(result_sentence,
                                                             "../solution")
                        return result_sentence


def search_for_combination_binary_search(anagram_product_sum, list_tuple_prime_sums,
                                         md5_hash="4624d200580677270a54ccff86b9610e"):
    for tuple1 in list_tuple_prime_sums:
        for tuple2 in list_tuple_prime_sums:

            last_prime_value_needed = anagram_product_sum / (tuple1[1] * tuple2[1])
            # Todo: fix the amount of ifs!

            if last_prime_value_needed.is_integer():
                index = binary_search.search(list_tuple_prime_sums, int(last_prime_value_needed))
                if index != -1:
                    tuple3 = list_tuple_prime_sums[index]
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
                                    list_tuple_prime_sums,
                                    chunk_index_start,
                                    chunk_index_stop,
                                    result_shared_mem_ref,
                                    md5_hash="4624d200580677270a54ccff86b9610e"):

    for tuple1 in list_tuple_prime_sums[chunk_index_start: chunk_index_stop]:
        for tuple2 in list_tuple_prime_sums:

            last_prime_value_needed = anagram_product_sum / (tuple1[1] * tuple2[1])
            # Todo: fix the amount of ifs!

            if last_prime_value_needed.is_integer():
                index = binary_search.search(list_tuple_prime_sums,
                                             int(last_prime_value_needed))
                if index != -1:
                    tuple3 = list_tuple_prime_sums[index]
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


# This method slowed down process
def check_append_words_char_limit(word1, word2, dict_of_char_limit):
    combined_words = word1 + word2
    dict_combined_word = dict()
    for char in combined_words:
        dict_combined_word[char] = wlc.value_to_increment_to_in_dict(dict_combined_word,
                                                                     char)
        if dict_combined_word[char] > dict_of_char_limit[char]:
            return False
    else:
        return True
