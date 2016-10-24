from processing import numpy_processing


def search_list_tuple(list_tuple_prime_sums, value_to_find):
    # list_tuple_word_prime[0] == word
    # list_tuple_word_prime[1] == prime_product_sum
    top = len(list_tuple_prime_sums) - 1
    bottom = 0

    while bottom <= top:
        mid = int(top + bottom / 2)

        # Key value in index 1
        if list_tuple_prime_sums[mid][1] == value_to_find:
            return mid
        elif list_tuple_prime_sums[mid][1] < value_to_find:
            bottom = mid + 1
        else:
            top = mid - 1

    # Todo: Maybe change -1 return
    # Return -1 if value not found
    return -1


def search_array(array_prime_sums, value_to_find):
    top = len(array_prime_sums) - 1
    bottom = 0

    while bottom <= top:

        mid = int((top + bottom) / 2)
        # Key value in index 1
        if array_prime_sums[mid] == value_to_find:

            return mid
        elif array_prime_sums[mid] < value_to_find:
            bottom = mid + 1
        else:
            top = mid - 1

    # Todo: Maybe change -1 return
    # Return -1 if value not found
    return -1


def get_list_same_products_from_array(list_tuple_word_prime, array_of_prime_sums, top_ref_array, bot_ref_array,
                                      index):
    # list_tuple_word_prime[0] == word
    # list_tuple_word_prime[1] == prime_product_sum

    array_value_to_look_form = array_of_prime_sums[index]
    length_of_array = len(array_of_prime_sums)

    top_index = index + 1
    bot_index = index - 1

    list_of_same_neighbors = list()

    word_one, word_two = numpy_processing.get_words_from_list_in_arrays(list_tuple_word_prime,
                                                                        top_ref_array,
                                                                        bot_ref_array,
                                                                        index)
    list_of_same_neighbors.append((word_one, word_two))

    while top_index < length_of_array:
        if array_of_prime_sums[top_index] == array_value_to_look_form:
            word_one, word_two = numpy_processing.get_words_from_list_in_arrays(list_tuple_word_prime,
                                                                                top_ref_array,
                                                                                bot_ref_array,
                                                                                top_index)
            list_of_same_neighbors.append((word_one, word_two))
            top_index += 1
        else:
            break

    while bot_index >= 0:
        if array_of_prime_sums[bot_index] == array_value_to_look_form:
            word_one, word_two = numpy_processing.get_words_from_list_in_arrays(list_tuple_word_prime,
                                                                                top_ref_array,
                                                                                bot_ref_array,
                                                                                bot_index)

            list_of_same_neighbors.append((word_one, word_two))
            bot_index -= 1
        else:
            break

    return list_of_same_neighbors


def get_list_of_one_word_candidates(list_tuple_word_prime, anagram_product_sum, index):
    value_to_look_for = anagram_product_sum
    length_of_array = len(list_tuple_word_prime)
    list_of_candidates = list()

    word_one = list_tuple_word_prime[index][0]
    list_of_candidates.append(word_one)

    top_index = index + 1
    bot_index = index - 1

    while top_index < length_of_array:
        if list_tuple_word_prime[top_index] == value_to_look_for:
            candidate = list_tuple_word_prime[top_index][0]
            list_of_candidates.append(candidate)
            top_index += 1
        else:
            break

    while bot_index >= 0:
        if list_tuple_word_prime[bot_index] == value_to_look_for:
            candidate = list_tuple_word_prime[bot_index][0]
            list_of_candidates.append(candidate)
            bot_index -= 1
        else:
            break

    return list_of_candidates
