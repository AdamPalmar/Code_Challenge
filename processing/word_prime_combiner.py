from md5_hashing import md5_hasher
from fileIO import file_writer


def check_three_tuples(tuple1, tuple2, tuple3, md5_hash="4624d200580677270a54ccff86b9610e"):
    tuple_hash = md5_hasher.md5_hash_sentence(tuple1[0] + " " + tuple2[0] + " " + tuple3[0])

    if tuple_hash == md5_hash:
        print("-------Found the hash------- ", tuple1, tuple2, tuple3)
        return True
    else:
        return False


# Todo: Make search run more then three loops
# Todo: Add early stop in for loops
# Todo: Is it a list of tuples though?
def search_for_combination(anagram_product_sum, list_tuple_prime_sums, md5_hash="4624d200580677270a54ccff86b9610e"):
    # print(anagram_product_sum)
    for tuple1 in list_tuple_prime_sums:
        for tuple2 in list_tuple_prime_sums:
            for tuple3 in list_tuple_prime_sums:
                product_sum = tuple1[1] * tuple2[1] * tuple3[1]

                if product_sum == anagram_product_sum:
                    # print(tuple1, tuple2, tuple3)
                    result = check_three_tuples(tuple1, tuple2, tuple3, md5_hash)
                    if result:
                        result_sentence = str(tuple1[0] + " " + tuple2[0] + " " + tuple3[0])
                        file_writer.write_solution_into_file(result_sentence,
                                                             "../solution")
                        return result_sentence


def search_for_combination_binary_search(anagram_product_sum, list_tuple_prime_sums,
                                         md5_hash="4624d200580677270a54ccff86b9610e"):
    # print(anagram_product_sum)
    for tuple1 in list_tuple_prime_sums:
        for tuple2 in list_tuple_prime_sums:

            last_prime_value_needed = anagram_product_sum / (tuple1[1] * tuple2[1])
            # Todo: fix the amount of ifs!
            if last_prime_value_needed.is_integer():
                index = binary_search(list_tuple_prime_sums, int(last_prime_value_needed))
                if index != -1:
                    tuple3 = list_tuple_prime_sums[index]
                    product_sum = tuple1[1] * tuple2[1] * tuple3[1]

                    if product_sum == anagram_product_sum:
                        # print(tuple1, tuple2, tuple3)
                        result = check_three_tuples(tuple1, tuple2, tuple3, md5_hash)
                        if result:
                            result_sentence = str(tuple1[0] + " " + tuple2[0] + " " + tuple3[0])
                            file_writer.write_solution_into_file(result_sentence,
                                                                 "../solution")
                            return result_sentence


def binary_search(list_tuple_prime_sums, value_to_find):
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
