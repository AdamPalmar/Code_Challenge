def search_list_tuple(list_tuple_prime_sums, value_to_find):
    # list_tuple_word_prime[0] == word
    # list_tuple_word_prime[1] == prime_product_sum
    top = len(list_tuple_prime_sums) - 1
    bottom = 0

    while bottom <= top:
        mid = int(top + bottom / 2)

        # Key value in index 1
        if list_tuple_prime_sums[mid][1] == value_to_find:
            # print("Looking at ", list_tuple_prime_sums[mid][1], "looking for ", value_to_find)
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
        mid = int(top + bottom / 2)

        # Key value in index 1
        if array_prime_sums[mid] == value_to_find:
            # print("Looking at ", list_tuple_prime_sums[mid][1], "looking for ", value_to_find)
            return mid
        elif array_prime_sums[mid] < value_to_find:
            bottom = mid + 1
        else:
            top = mid - 1

    # Todo: Maybe change -1 return
    # Return -1 if value not found
    return -1


def get_list_of_same_neighbors_for_array(list_tuple_word_prime, array_prime_sums, index):
    # list_tuple_word_prime[0] == word
    # list_tuple_word_prime[1] == prime_product_sum

    array_value_to_look_form = array_prime_sums[index]
    length_of_array = len(array_prime_sums)

    top_index = index + 1
    bot_index = index - 1

    list_of_same_neighbors = list()

    while top_index < length_of_array:
        if array_prime_sums[top_index] == array_value_to_look_form:
            list_of_same_neighbors.append(list_tuple_word_prime[top_index][0])
            top_index += 1
        else:
            break

    while bot_index >= 0:
        if array_prime_sums[bot_index] == array_value_to_look_form:
            list_of_same_neighbors.append(list_tuple_word_prime[bot_index][0])
            bot_index -= 1
        else:
            break

    return list_of_same_neighbors
