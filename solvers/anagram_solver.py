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

    def solve_anagram(self, path_to_file, anagram_sentence, md5_hash):
        pass


class SingleCpuSolver(Solver):
    def __init__(self, **kwargs):
        super(SingleCpuSolver, self).__init__()
        self._attributes = kwargs
