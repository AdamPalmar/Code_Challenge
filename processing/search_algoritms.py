from fileIO import file_writer
from processing import binary_search, numpy_processing
from processing import word_checking as word_check


def search_multi_core_binary_search_numpy(anagram_product_sum,
                                          list_tuple_word_prime,
                                          chunk_index_start,
                                          chunk_index_stop,
                                          result_shared_mem_ref,
                                          md5_hash="4624d200580677270a54ccff86b9610e"):
    array_of_word_prime_values = numpy_processing.convert_list_tuple_into_numpy_array(list_tuple_word_prime)

    found_correct, sentence = word_check.check_for_one_word(anagram_product_sum,
                                                            array_of_word_prime_values,
                                                            list_tuple_word_prime,
                                                            md5_hash)

    if found_correct:
        result_shared_mem_ref.value = sentence
        return

    num_words = len(array_of_word_prime_values)

    (product_array,
     top_ref_word,
     bot_ref_word) = numpy_processing.get_prime_product_of_arrays(num_words, array_of_word_prime_values)

    found_correct, sentence = word_check.check_for_combinations_of_two(anagram_product_sum, product_array,
                                                                       list_tuple_word_prime,
                                                                       top_ref_word, bot_ref_word, md5_hash)

    if found_correct:
        result_shared_mem_ref.value = sentence
        return

    for index, product_sum in enumerate(array_of_word_prime_values[chunk_index_start: chunk_index_stop]):

        prime_product_needed = anagram_product_sum / product_sum

        if prime_product_needed.is_integer():

            index_of_product_array = binary_search.search_array(product_array, int(prime_product_needed))

            # This means a anagram was found
            if index_of_product_array != -1:
                word_one = numpy_processing.get_word_from_list_in_array(list_tuple_word_prime, index, chunk_index_start)

                list_of_candidate_words = binary_search.get_list_same_products_from_array(list_tuple_word_prime,
                                                                                          product_array,
                                                                                          top_ref_word,
                                                                                          bot_ref_word,
                                                                                          index_of_product_array)

                word_check.check_hash_for_three_words(word_one, list_of_candidate_words, md5_hash,
                                                      result_shared_mem_ref)
