from preproccessing import word_prime_converter as wpc
from processing import word_prime_combiner


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

    def solve_anagram(self):
        pass


class SingleCpuSolver(Solver):
    def __init__(self, **kwargs):
        super(SingleCpuSolver, self).__init__()
        self._attributes = kwargs

    def solve_anagram(self):
        word_prime_combiner.seach_for_combination(wpc.get_product_sum_anagram_sentence(),
                                                  wpc.get_sorted_dict_char_to_prime("../clean_wordlist_invalid_num_chars"))


if __name__ == "__main__":
    solver = SingleCpuSolver()
    solver.solve_anagram()

