from fileIO import file_reader, file_writer
from utilities import utility


def remove_words_with_invalid_char(list_of_words, anagram_sentence):
    set_of_character_in_anagram = set()
    list_of_clean_words = []

    for char in utility.remove_space_from_sentence(anagram_sentence):
        set_of_character_in_anagram.add(char)

    for word_in_file in utility.remove_empty_space_in_list(list_of_words):
        for char in word_in_file:
            if char not in set_of_character_in_anagram:
                break
        else:
            # This happens if for loop is run without the break
            list_of_clean_words.append(word_in_file)
            continue

    return list_of_clean_words


def dict_of_char_in_anagram_sentence(anagram_sentence):
    dictionary_of_chars = dict()
    for char in utility.remove_space_from_sentence(anagram_sentence):
        dictionary_of_chars[char] = value_to_increment_to_in_dict(dictionary_of_chars, char)

    return dictionary_of_chars


def value_to_increment_to_in_dict(dictionary, char):
    if char not in dictionary:
        return 1
    else:
        return dictionary[char] + 1


def remove_words_with_too_many_of_one_char(list_of_words, anagram_sentence):
    list_of_clean_words = []
    d = dict_of_char_in_anagram_sentence(utility.remove_space_from_sentence(anagram_sentence))

    for word in utility.remove_empty_space_in_list(list_of_words):
        dict_current_word = dict()
        for char in word:
            dict_current_word[char] = value_to_increment_to_in_dict(dict_current_word, char)
            if dict_current_word[char] > d[char]:
                break
        else:
            list_of_clean_words.append(word)
            continue

    return list_of_clean_words


# For removing non valid words from list.
#Todo: refactor method so it can be tested
def clean_wordlist(anagram_sentence, path_to_wordlist, path_to_clean_wordlist="clean_wordlist_invalid_num_chars"):
    temp_file_path = "../clean_wordlist"
    l = remove_words_with_invalid_char(file_reader.read_file_into_list(path_to_wordlist), anagram_sentence)
    file_writer.write_list_into_file(l, temp_file_path)
    l = remove_words_with_too_many_of_one_char(file_reader.read_file_into_list(temp_file_path), anagram_sentence)
    file_writer.write_list_into_file(l, path_to_clean_wordlist)
