import numpy
from fileIO import file_reader


def remove_space_from_sentence(sentence):
    return sentence.replace(" ", "")


def sort_dict(dict_prime_sums):
    return sorted(dict_prime_sums.items(), key=lambda x: x[1])


def dict_words_to_prime_product_sums(list_of_words, dict_char_to_prime):
    dict_of_word_prime_products = dict()

    for word in list_of_words:
        product_sum = 1
        for character in word:
            product_sum *= dict_char_to_prime[character]
        dict_of_word_prime_products[word] = product_sum

    return dict_of_word_prime_products


def prime_product_sum_of_anagram_sentence(anagram_sentence, dict_char_to_prime):
    product_sum = 1
    for character in anagram_sentence:
        product_sum *= dict_char_to_prime[character]
    return product_sum


def dict_prime_numbers_to_anagram_character(anagram_sentence):
    dict_of_prime_number_mapping = dict()
    set_of_characters_in_anagram = set(remove_space_from_sentence(anagram_sentence))

    # Todo: Replace list with prime number generator
    # amount of prime numbers must at least match number of unique characters in anagram sentence.

    list_of_prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                             97, 101,
                             103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
                             197, 199,
                             211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
                             313, 317,
                             331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]

    # Todo: For optimization round. change such that most frequent characters get low primenumbers
    # Currently the anagram_characters are picked randomly
    for index, character in enumerate(set_of_characters_in_anagram):
        dict_of_prime_number_mapping[character] = list_of_prime_numbers[index]

    return dict_of_prime_number_mapping


def get_sorted_dict_char_to_prime(path_to_file, anagram_sentence="poultryoutwitsants"):
    dict_prime_char = dict_prime_numbers_to_anagram_character(anagram_sentence)

    dict_word_prime_sums = dict_words_to_prime_product_sums(file_reader.read_file_into_list(path_to_file),
                                                            dict_prime_char)

    sorted_dict = sort_dict(dict_word_prime_sums)

    return sorted_dict


def get_product_sum_anagram_sentence(anagram_sentence="poultryoutwitsants"):
    dict_prime_char = dict_prime_numbers_to_anagram_character(anagram_sentence)
    return prime_product_sum_of_anagram_sentence(anagram_sentence, dict_prime_char)



