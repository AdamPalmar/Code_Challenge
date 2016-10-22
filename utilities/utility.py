def remove_space_from_sentence(sentence):
    return sentence.replace(" ", "")


def sort_dict(dict_prime_sums):
    return sorted(dict_prime_sums.items(), key=lambda x: x[1])
