import numpy as np
from profiler import line_profiling


def element_wise_multiply_arrays(array_1, array_2):
    return np.multiply(array_1, array_2)


def sort_array(numpy_array):
    return np.sort(numpy_array)


def init_arrays(array_size):
    top_array = np.zeros(shape=(array_size,), dtype=np.uint64)
    bottom_array = np.zeros(shape=(array_size,), dtype=np.uint64)

    top_array_ref_to_list_word = np.zeros(shape=(array_size,), dtype=np.uint64)
    bottom_array_ref_to_list_word = np.zeros(shape=(array_size,), dtype=np.uint64)

    return (top_array,
            bottom_array,
            top_array_ref_to_list_word,
            bottom_array_ref_to_list_word)


# @line_profiling.profile(follow=[])
def get_prime_product_of_arrays(num_words, array_of_words):
    """
    This array will be used to do binary search in
    to find combinations that match anagram prime product sum.

    :param num_words:
    :param array_of_words:
    :return: tuple( element-wise product arrays,top_ref_array, bot_ref_array)

    """
    array_size = int(num_words * (num_words - 1) / 2)

    top_array, bottom_array, top_ref_word_array, bot_ref_word_array = init_arrays(array_size)

    range_array = np.arange(0, num_words)

    start_index = 0
    for index, num in enumerate(range(num_words - 1, 0, -1)):
        stop_index = start_index + num

        # Array of prime product sums
        top_array[start_index: stop_index] = array_of_words[index]
        bottom_array[start_index: stop_index] = array_of_words[-num:]

        # Index into list for the two arrays to find original word
        top_ref_word_array[start_index: stop_index] = index
        # bot_ref_word_array[start_index: stop_index] = range(index + 1, num_words)
        bot_ref_word_array[start_index: stop_index] = range_array[index + 1:]

        start_index += num

    result_array = element_wise_multiply_arrays(top_array, bottom_array)

    return sort_product_array_with_top_bot(result_array, top_ref_word_array, bot_ref_word_array)


def sort_product_array_with_top_bot(result_array, top_ref_word_list, bot_ref_word_list):
    permutation = result_array.argsort()
    result_array = result_array[permutation]
    top_ref_word_list = top_ref_word_list[permutation]
    bot_ref_word_list = bot_ref_word_list[permutation]
    return result_array, top_ref_word_list, bot_ref_word_list


def convert_list_tuple_into_numpy_array(list_of_tuple):
    array_size = len(list_of_tuple)

    numpy_array = np.zeros(shape=(array_size,), dtype=np.uint64)

    for index, tuple in enumerate(list_of_tuple):
        # The value is in index 1
        numpy_array[index] = tuple[1]

    return numpy_array


def get_word_from_list_in_array(list_of_tuple, index, chunck_index_start):
    return list_of_tuple[index + chunck_index_start][0]


def get_words_from_list_in_arrays(list_of_tuple, top_ref_array, bottom_ref_array, index):
    word_1 = list_of_tuple[top_ref_array[index]][0]
    word_2 = list_of_tuple[bottom_ref_array[index]][0]

    return word_1, word_2
