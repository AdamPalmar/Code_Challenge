from preproccessing import word_prime_converter as wpc
from md5_hashing import md5_hasher
from fileIO import file_writer


def check_three_tuples(tuple1, tuple2, tuple3, md5_hash="4624d200580677270a54ccff86b9610e"):
    list_of_hashed = []
    list_of_hashed.append(md5_hasher.md5_hash_sentence(tuple1[0] + " " + tuple2[0] + " " + tuple3[0]))
    list_of_hashed.append(md5_hasher.md5_hash_sentence(tuple1[0] + " " + tuple3[0] + " " + tuple2[0]))
    list_of_hashed.append(md5_hasher.md5_hash_sentence(tuple2[0] + " " + tuple2[0] + " " + tuple1[0]))
    list_of_hashed.append(md5_hasher.md5_hash_sentence(tuple2[0] + " " + tuple1[0] + " " + tuple3[0]))
    list_of_hashed.append(md5_hasher.md5_hash_sentence(tuple3[0] + " " + tuple2[0] + " " + tuple1[0]))
    list_of_hashed.append(md5_hasher.md5_hash_sentence(tuple3[0] + " " + tuple1[0] + " " + tuple2[0]))

    for hash in list_of_hashed:
        if hash == md5_hash:
            print("-------Found the hash------- ", tuple1, tuple2, tuple3)
            file_writer.write_solution_into_file(str(tuple1[0] + " " + tuple2[0] + " " + tuple3[0]), "../solution")


def seach_for_combination(anagram_product_sum, dict_prime_sums):
    print(anagram_product_sum)
    for tuple1 in dict_prime_sums:
        for tuple2 in dict_prime_sums:
            for tuple3 in dict_prime_sums:
                product_sum = tuple1[1] * tuple2[1] * tuple3[1]
                if (product_sum == anagram_product_sum):
                    print(tuple1, tuple2, tuple3)
                    check_three_tuples(tuple1, tuple2, tuple3)

    print(len(dict_prime_sums))



# seach_for_combination(wpc.get_product_sum_anagram_sentence(),
#                       wpc.get_sorted_dict_char_to_prime("../clean_wordlist_invalid_num_chars"))
#

