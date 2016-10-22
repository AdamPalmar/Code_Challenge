def search(list_tuple_prime_sums, value_to_find):
    top = len(list_tuple_prime_sums) - 1
    bottom = 0

    while bottom <= top:
        mid = int(top + bottom / 2)

        # Todo: Look at the neighbors "abc" == "cba" == samevalue != hash
        # Key value in index 1
        if list_tuple_prime_sums[mid][1] == value_to_find:
            # print("Looking at ", list_tuple_prime_sums[mid][1], "looking for ", value_to_find)
            return mid
        elif list_tuple_prime_sums[mid][1] < value_to_find:
            bottom = mid + 1
        else:
            top = mid - 1

    # Todo: Mabye change -1 return
    # Return -1 if value not found
    return -1