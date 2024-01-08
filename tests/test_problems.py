import pytest

from exact_cover_py import exact_cover

import problems

all_problems = [
    problem for problem in problems.__dict__ if "_problem" in problem
]

# make a set of sorted tuples
def canonical(iterable):
    return set(tuple(sorted(x)) for x in iterable)


def define_test(problem_name):
    """
    for a given problem found defined in problems.py
    say small_trimino_problem
    we define a derived function named like
    say test_small_trimino_problem
    """

    def test_solutions(problem):
        input = problem['data']
        canonical_solutions = canonical(problem['solutions'])
        try:
            canonical_computed = set(tuple(sorted(x)) for x in exact_cover(input))
            assert canonical_computed == canonical_solutions
        except StopIteration:
            assert problem['solutions'] == set()
    problem = problems.__dict__[problem_name]()
    test_name = f"test_{problem_name}"
    # assign the global variable test_name to the newly defined function
    globals()[test_name] = lambda: test_solutions(problem)

for problem in all_problems:
    define_test(problem)
