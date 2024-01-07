import pytest

from exact_cover_py import exact_cover

import problems

all_problems = [
    problem for problem in problems.__dict__ if "_problem" in problem
]

# for a given problem found defined in problems.py
# say small_trimino_problem
# we define a derived function named like
# say test_solution1_small_trimino_problem

def define_solution1_test(problem_name):
    def test_solution1(problem):
        input = problem['data']
        try:
            computed = next(exact_cover(input))
        except StopIteration:
            computed = None
        if problem['solution1'] == "UNTESTED":
            print(f"{problem_name} solution1 is {computed}")
        else:
            assert set(computed) == set(problem['solution1'])
    problem = problems.__dict__[problem_name]()
    test_name = f"test_solution1_{problem_name}"
    globals()[test_name] = lambda: test_solution1(problem)


def mylen(gen):
    return sum(map(lambda x: 1, gen))

# same with count
def define_count_test(problem_name):
    def test_count(problem):
        input = problem['data']
        try:
            computed = mylen(exact_cover(input))
        except StopIteration:
            computed = 0
        if problem['count'] == "UNTESTED":
            print(f"{problem_name} count is {computed}")
        else:
            assert computed == problem['count']
    problem = problems.__dict__[problem_name]()
    test_name = f"test_count_{problem_name}"
    globals()[test_name] = lambda: test_count(problem)


for problem in all_problems:
    define_solution1_test(problem)
    define_count_test(problem)
