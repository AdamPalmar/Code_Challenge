def remove_space_from_sentence(sentence):
    return sentence.replace(" ", "")


def get_sorted_list_of_tuple_from_dict(dict_prime_sums):
    return sorted(dict_prime_sums.items(), key=lambda x: x[1])


def remove_empty_space_in_list(list_of_words):
    for word in list_of_words:

        if word == " ":
            list_of_words.remove(word)

    list_of_words = list(filter(None, list_of_words))
    return list_of_words


def chunk_index_gen(list_tuple_char_to_prime, num_cores):
    for i in range(0, len(list_tuple_char_to_prime), num_cores):
        yield (i, i + num_cores)
