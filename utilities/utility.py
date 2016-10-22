def remove_space_from_sentence(sentence):
    return sentence.replace(" ", "")


def sort_dict(dict_prime_sums):
    return sorted(dict_prime_sums.items(), key=lambda x: x[1])


def remove_empty_space_in_list(list_of_words):
    for word in list_of_words:
        if word == "" or word == " ":
            list_of_words.remove(word)

    return list_of_words


