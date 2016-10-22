import os
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



print(os.getcwd())
print(os.path)
