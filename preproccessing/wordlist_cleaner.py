from fileIO import file_reader, file_writer


def remove_words_with_invalid_char(list_of_words, anagram_sentence):
    set_of_character_in_anagram = set()
    list_of_clean_words = []

    for char in anagram_sentence.replace(" ", ""):
        set_of_character_in_anagram.add(char)
    # print(set_of_character_in_anagram)

    for word_in_file in list_of_words:
        for char in word_in_file:
            if char not in set_of_character_in_anagram:
                # print("Remove word", character, word_in_file)
                break
        else:
            # This happens if for loop is run without the break
            list_of_clean_words.append(word_in_file)
            continue

    return list_of_clean_words


def dict_of_char_in_anagram_sentence(anagram_sentence):
    dictionary_of_chars = dict()
    for char in anagram_sentence:
        dictionary_of_chars[char] = value_to_increment_to_in_dict(dictionary_of_chars, char)

    return dictionary_of_chars


def value_to_increment_to_in_dict(dictionary, char):
    if char not in dictionary:
        return 1
    else:
        return dictionary[char] + 1


def remove_words_with_too_many_of_one_char(list_of_words, anagram_sentence):
    list_of_clean_words = []
    d = dict_of_char_in_anagram_sentence(anagram_sentence)

    for word in list_of_words:
        dict_current_word = dict()
        # Todo: fix indexing
        for char in word[:-1]:
            dict_current_word[char] = value_to_increment_to_in_dict(dict_current_word, char)
            if dict_current_word[char] > d[char]:
                break
        else:
            list_of_clean_words.append(word)
            continue

    print(d)
    print(len(list_of_clean_words))
    return list_of_clean_words

# For removing non valid words from list.

# l = remove_words_with_invalid_char(file_reader.read_file_into_list(), "poultry outwits ants\n")
# file_writer.write_list_into_file(l, "../clean_wordlist_invalid_chars")
# l = remove_words_with_too_many_of_one_char(file_reader.read_file_into_list("../clean_wordlist"), "poultryoutwitsants")
# file_writer.write_list_into_file(l, "../clean_wordlist_invalid_num_chars")
