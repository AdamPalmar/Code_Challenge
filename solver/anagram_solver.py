from preproccessing import word_prime_converter as wpc
from preproccessing import wordlist_cleaner
from processing import search_algoritms
from utilities import utility
from ctypes import c_char_p
import multiprocessing
import time


class MultipleCpuSolverBinaryNumpySearch:
    def __init__(self, **kwargs):
        self._attributes = kwargs

    def solve_anagram(self, anagram_sentence, path_to_wordlist, md5_hash="4624d200580677270a54ccff86b9610e"):

        clean_list = wordlist_cleaner.get_clean_wordlist(anagram_sentence,
                                                         path_to_wordlist)

        anagram_prime_product_sum = wpc.get_product_sum_anagram_sentence(anagram_sentence)
        list_tuple_char_to_prime = wpc.get_sorted_list_tuple_char_to_prime(clean_list, anagram_sentence)

        return self.distribute_work(list_tuple_char_to_prime, anagram_prime_product_sum, md5_hash)

    def distribute_work(self, list_tuple_char_to_prime, anagram_prime_product_sum, md5_hash):
        # I have a intel i7-2700k processor
        # It has 4 cores.
        num_cores = 4

        chunks = int(len(list_tuple_char_to_prime) / num_cores)

        chunk_generator = utility.chunk_index_gen(list_tuple_char_to_prime, chunks)

        return self.launch_workers(anagram_prime_product_sum,
                                   list_tuple_char_to_prime,
                                   chunk_generator,
                                   md5_hash)

    def launch_workers(self, anagram_prime_product_sum,
                       list_tuple_char_to_prime,
                       chunk_index_generator,
                       md5_hash):
        list_of_workers = []
        manager = multiprocessing.Manager()
        result_sentence = manager.Value(c_char_p, "No result")
        for list_chunk_index in chunk_index_generator:
            process = multiprocessing.Process(target=search_algoritms.search_multi_core_binary_search_numpy,
                                              args=(anagram_prime_product_sum,
                                                    list_tuple_char_to_prime,
                                                    list_chunk_index[0],
                                                    list_chunk_index[1],
                                                    result_sentence,
                                                    md5_hash))
            list_of_workers.append(process)

        for worker in list_of_workers:
            worker.start()

        for worker in list_of_workers:
            worker.join()

        return result_sentence.value


def main(anagram_sentence, path_to_wordlist):
    solver = MultipleCpuSolverBinaryNumpySearch()

    print("Starting")
    t = time.time()
    result = solver.solve_anagram(anagram_sentence, "../wordlist")
    print(result, "Original sentence returned")
    print(time.time() - t, "time")
    print("Done")
    return result


if __name__ == "__main__":
    anagram_sentence = "poultry outwits ants"
    path_to_wordlist = "../wordlist"
    main(anagram_sentence=anagram_sentence,
         path_to_wordlist=path_to_wordlist)
