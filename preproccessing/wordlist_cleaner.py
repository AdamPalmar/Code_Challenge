from fileIO import file_reader, file_writer

def remove_words_with_invalid_char(list_of_words_from_file, anagram_sentence):

    counter = 0
    set_of_character_in_anagram = set()
    list_of_clean_words = []
    for character in anagram_sentence:
        if character == " ":
            pass
        else:
            set_of_character_in_anagram.add(character)
    print(set_of_character_in_anagram)

    for word_in_file in list_of_words_from_file:
        for character in word_in_file:
            if character not in set_of_character_in_anagram:
                print("Remove word", character , word_in_file)
                break
        else:
            list_of_clean_words.append(word_in_file)
            continue

    return list_of_clean_words




# l = remove_words_with_invalid_char(file_reader.read_file_into_list(),"poultry outwits ants\n")
# file_writer.write_list_into_file(l,"../clean_wordlist")

