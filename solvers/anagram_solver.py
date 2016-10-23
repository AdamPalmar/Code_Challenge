from preproccessing import word_prime_converter as wpc
from preproccessing import wordlist_cleaner
from processing import search_algoritms
from ctypes import c_char_p
from profiler import line_profiling
import multiprocessing

import time


class Solver:
    """
    This is the base class for solvers for the anagram problem.
    All classes that solves the anagram problem shall
    inherit from this class.
    """

    def __init__(self, **kwargs):
        self._attributes = kwargs

    def set_attributes(self, key, value):
        self._attributes = [key] = value
        return

    def get_attributes(self, key):
        return self._attributes.get(key, None)

    def solve_anagram(self, anagram_sentence, path_to_wordlist):
        pass


class SingleCpuSolver(Solver):
    def __init__(self, **kwargs):
        super(SingleCpuSolver, self).__init__()
        self._attributes = kwargs

    def solve_anagram(self, anagram_sentence, path_to_wordlist):
        clean_list = wordlist_cleaner.get_clean_wordlist(anagram_sentence,
                                                         path_to_wordlist)

        anagram_prime_product_sum = wpc.get_product_sum_anagram_sentence(anagram_sentence)
        list_tuple_char_to_prime = wpc.get_sorted_list_tuple_char_to_prime(clean_list)

        search_algoritms.search_for_combination(anagram_prime_product_sum,
                                                list_tuple_char_to_prime)


class SingleCpuSolverBinarySearch(Solver):
    def __init__(self, **kwargs):
        super(SingleCpuSolverBinarySearch, self).__init__()
        self._attributes = kwargs

    def solve_anagram(self, anagram_sentence, path_to_wordlist):
        print("Preprocessing")
        clean_list = wordlist_cleaner.get_clean_wordlist(anagram_sentence, path_to_wordlist)
        print("Searching")

        anagram_prime_product_sum = wpc.get_product_sum_anagram_sentence(anagram_sentence)
        list_tuple_char_to_prime = wpc.get_sorted_list_tuple_char_to_prime(clean_list)

        search_algoritms.search_for_combination_binary_search(anagram_prime_product_sum,
                                                              list_tuple_char_to_prime)


class MultipleCpuSolverBinarySearch(Solver):
    def __init__(self, **kwargs):
        super(MultipleCpuSolverBinarySearch, self).__init__()
        self._attributes = kwargs

    def solve_anagram(self, anagram_sentence, path_to_wordlist):
        print("Preprocessing")
        clean_list = wordlist_cleaner.get_clean_wordlist(anagram_sentence,
                                                         path_to_wordlist)
        print("Searching")

        anagram_prime_product_sum = wpc.get_product_sum_anagram_sentence(anagram_sentence)
        list_tuple_char_to_prime = wpc.get_sorted_list_tuple_char_to_prime(clean_list)

        self.distribute_work(list_tuple_char_to_prime, anagram_prime_product_sum)

    def distribute_work(self, list_tuple_char_to_prime, anagram_prime_product_sum):

        # I have a intel i7-2700k processor
        # It has 4 cores.
        num_cores = 4

        chunks = int(len(list_tuple_char_to_prime) / num_cores)

        # Todo: it is not possible to shuffle list and only use index
        # Else i need to copy list and send it aswell
        # random.shuffle(list_tuple_char_to_prime, random.random)

        chunk_generator = self.chunk_index_gen(list_tuple_char_to_prime, chunks)

        self.launch_workers(anagram_prime_product_sum,
                            list_tuple_char_to_prime,
                            chunk_generator)

    def chunk_index_gen(self, list_tuple_char_to_prime, num_cores):
        for i in range(0, len(list_tuple_char_to_prime), num_cores):
            yield (i, i + num_cores)

    def launch_workers(self, anagram_prime_product_sum,
                       list_tuple_char_to_prime,
                       chunk_index_generator):

        list_of_workers = []
        manager = multiprocessing.Manager()
        result_sentence = manager.Value(c_char_p, "No result")
        for list_chunk_index in chunk_index_generator:
            process = multiprocessing.Process(target=search_algoritms.search_multi_core_binary_search,
                                              args=(anagram_prime_product_sum,
                                                    list_tuple_char_to_prime,
                                                    list_chunk_index[0],
                                                    list_chunk_index[1],
                                                    result_sentence))
            list_of_workers.append(process)

        for worker in list_of_workers:
            worker.start()
            # print(worker.pid)

        for worker in list_of_workers:
            # print(worker.pid)
            worker.join()

        print(result_sentence.value)

        return result_sentence.value


class MultipleCpuSolverBinaryNumpySearch(Solver):
    def __init__(self, **kwargs):
        super(MultipleCpuSolverBinaryNumpySearch, self).__init__()
        self._attributes = kwargs

    def solve_anagram(self, anagram_sentence, path_to_wordlist):
        print("Preprocessing")

        clean_list = wordlist_cleaner.get_clean_wordlist(anagram_sentence,
                                                         path_to_wordlist)
        print("Searching")

        anagram_prime_product_sum = wpc.get_product_sum_anagram_sentence(anagram_sentence)
        list_tuple_char_to_prime = wpc.get_sorted_list_tuple_char_to_prime(clean_list)

        self.distribute_work(list_tuple_char_to_prime, anagram_prime_product_sum)

    def distribute_work(self, list_tuple_char_to_prime, anagram_prime_product_sum):
        # I have a intel i7-2700k processor
        # It has 4 cores.
        num_cores = 1

        chunks = int(len(list_tuple_char_to_prime) / num_cores)

        # Todo: it is not possible to shuffle list and only use index
        # Else i need to copy list and send it aswell
        # random.shuffle(list_tuple_char_to_prime, random.random)

        chunk_generator = self.chunk_index_gen(list_tuple_char_to_prime, chunks)

        self.launch_workers(anagram_prime_product_sum,
                            list_tuple_char_to_prime,
                            chunk_generator)

    def chunk_index_gen(self, list_tuple_char_to_prime, num_cores):
        for i in range(0, len(list_tuple_char_to_prime), num_cores):
            yield (i, i + num_cores)

    def launch_workers(self, anagram_prime_product_sum,
                       list_tuple_char_to_prime,
                       chunk_index_generator):
        list_of_workers = []
        manager = multiprocessing.Manager()
        result_sentence = manager.Value(c_char_p, "No result")
        for list_chunk_index in chunk_index_generator:
            process = multiprocessing.Process(target=search_algoritms.search_multi_core_binary_search_numpy,
                                              args=(anagram_prime_product_sum,
                                                    list_tuple_char_to_prime,
                                                    list_chunk_index[0],
                                                    list_chunk_index[1],
                                                    result_sentence))
            list_of_workers.append(process)

        for worker in list_of_workers:
            worker.start()
            print(worker.pid, "worker id")

        for worker in list_of_workers:
            # print(worker.pid)
            worker.join()

        print(result_sentence.value, "result sentence")

        return result_sentence.value


def main():
    # solver = MultipleCpuSolverBinarySearch()
    solver = MultipleCpuSolverBinaryNumpySearch()

    print("Starting")
    t = time.time()
    solver.solve_anagram("poultry outwits ants", "../wordlist")
    print(time.time() - t, "time")
    print("Done")


if __name__ == "__main__":
    main()
