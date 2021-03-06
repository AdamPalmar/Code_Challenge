from processing import binary_search
from hasher import md5_hasher
from fileIO import file_writer
import itertools


def check_for_one_word(anagram_product_sum,
                       array_of_word_values,
                       list_tuple_word_prime,
                       md5_hash):
    index = binary_search.search_array(array_prime_sums=array_of_word_values,
                                       value_to_find=anagram_product_sum)

    if index != -1:
        list_of_candidate_words = binary_search.get_list_of_one_word_candidates(list_tuple_word_prime,
                                                                                anagram_product_sum,
                                                                                index)
        is_correct_hash, sentence = check_hash_one_word_list(list_of_candidate_words, md5_hash)

        if is_correct_hash:
            return True, sentence

    return False, None


def check_for_combinations_of_two(anagram_product_sum,
                                  product_array,
                                  list_tuple_word_prime,
                                  top_ref_word,
                                  bot_ref_word,
                                  md5_hash):
    index_of_product_array = binary_search.search_array(product_array, int(anagram_product_sum))

    if index_of_product_array != -1:

        list_of_candidate_words = binary_search.get_list_same_products_from_array(list_tuple_word_prime,
                                                                                  product_array,
                                                                                  top_ref_word,
                                                                                  bot_ref_word,
                                                                                  index_of_product_array)

        is_correct_hash, sentence = check_hash_for_list_pair_combinations(list_of_candidate_words, md5_hash)

        if is_correct_hash:
            return True, sentence

    return False, None


def check_hash_for_three_words(word_one, list_of_candidates, md5_hash, result_shared_mem_ref):
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


def check_hash_for_list_pair_combinations(list_of_word_pairs, md5_hash):
    for word_pair in list_of_word_pairs:
        combinations = itertools.permutations(word_pair)
        for combination in combinations:
            sentence = combination[0] + " " + combination[1]
            word_hash = md5_hasher.md5_hash_sentence(sentence)

            if word_hash == md5_hash:
                return True, sentence

    else:
        return False, None


def check_hash_one_word_list(list_of_word, md5_hash):
    for word in list_of_word:
        word_hash = md5_hasher.md5_hash_sentence(word)

        if word_hash == md5_hash:
            return True, word
    else:
        return False, None


def save_solution(sentence):
    print("--------Found the hash------", sentence)
    file_writer.write_solution_into_file(sentence, "../solution")
