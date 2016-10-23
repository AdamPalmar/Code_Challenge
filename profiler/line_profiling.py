from line_profiler import LineProfiler


def profile(follow=[]):
    def inner(func):
        def profiled_function(*args, **kwargs):
            try:
                profiler = LineProfiler()
                profiler.add_function(func)
                for f in follow:
                    profiler.add_function(f)
                profiler.enable_by_count()
                return func(*args, **kwargs)
            finally:
                profiler.print_stats()

        return profiled_function

    return inner
