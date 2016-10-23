from md5_hashing import md5_hasher
from fileIO import file_writer
from processing import binary_search, numpy_processing
from preproccessing import wordlist_cleaner as wlc

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
        print("--------Found the hash------", word_one, word_two, word_three)
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



#Todo: work in progress
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

    # product_array = numpy_processing.sort_array(product_array)

    for index, product_sum in enumerate(array_of_word_values[chunk_index_start: chunk_index_stop]):

        # anagram_product_sum = 547236300691459849470

        prime_product_needed = anagram_product_sum / product_sum

        if prime_product_needed.is_integer():

            index_of_product_array = binary_search.search_array(product_array, int(prime_product_needed))

            if index_of_product_array != -1:

                result_shared_mem_ref.value = index_of_product_array
                word_one = numpy_processing.get_word_from_list_in_array(list_tuple_word_prime, index, chunk_index_start)

                list_of_candidate_words = binary_search.get_list_of_same_neighbors_for_array(list_tuple_word_prime,
                                                                                             product_array,
                                                                                             top_ref_word,
                                                                                             bot_ref_word,
                                                                                             index + chunk_index_start)
                # print(list_of_candidate_words, "Candidate words")

                word_two, word_three = numpy_processing.get_words_from_list_in_arrays(list_tuple_word_prime,
                                                                                      top_ref_word,
                                                                                      bot_ref_word,
                                                                                      index_of_product_array)

                # print(word_one, word_two, word_three)

                # Todo: The algorithm should also look at neightbors with same product!

                result = check_three_words(word_one, word_two, word_three, md5_hash)

                if result:
                    result_sentence = str(word_one + " " + word_two + " " + word_three)
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


a = 3109981535661 * 3216705405595
print(a)
