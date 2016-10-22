from fileIO import file_reader
from prime_number_generator import prime_generator
from utilities import utility


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
    for character in utility.remove_space_from_sentence(anagram_sentence):
        product_sum *= dict_char_to_prime[character]
    return product_sum


def dict_prime_numbers_to_anagram_character(anagram_sentence):
    dict_of_prime_number_mapping = dict()
    set_of_characters_in_anagram = set(utility.remove_space_from_sentence(anagram_sentence))

    # Converting to list to avoid random enumeration of set.

    list_of_character_in_anagram = list(set_of_characters_in_anagram)
    list_of_character_in_anagram = sorted(list_of_character_in_anagram)

    list_of_prime_numbers = prime_generator.get_list_of_prime_numbers()

    # Todo: For optimization round. change such that most frequent characters get low primenumbers
    # Currently the anagram_characters are picked randomly
    for index, character in list(enumerate(list_of_character_in_anagram)):
        dict_of_prime_number_mapping[character] = list_of_prime_numbers[index]

    return dict_of_prime_number_mapping


def get_sorted_list_tuple_char_to_prime(path_to_file, anagram_sentence="poultryoutwitsants"):
    anagram_sentence = utility.remove_space_from_sentence(anagram_sentence)
    dict_prime_char = dict_prime_numbers_to_anagram_character(anagram_sentence)

    dict_word_prime_sums = dict_words_to_prime_product_sums(file_reader.read_file_into_list(path_to_file),
                                                            dict_prime_char)

    sorted_dict = utility.get_sorted_list_of_tuple_from_dict(dict_word_prime_sums)

    return sorted_dict


def get_product_sum_anagram_sentence(anagram_sentence="poultryoutwitsants"):
    dict_prime_char = dict_prime_numbers_to_anagram_character(anagram_sentence)
    return prime_product_sum_of_anagram_sentence(anagram_sentence, dict_prime_char)
