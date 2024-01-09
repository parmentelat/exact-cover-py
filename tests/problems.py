import numpy as np
import pandas as pd

DTYPE_FOR_ARRAY = bool


# one specific problem that I had trouble with
# originally based on solving the trivial problem
# of arranging 2 identical triminos on a 3x3 board

#    +--+
#    |  |
# +--+--+
# |  |  |
# +--+--+

# +--+--+--+
# |xx|  |xx|
# +--+--+--+
# |  |  |  |
# +--+--+--+
# |xx|  |  |
# +--+--+--+


# this problem has 2 solutions
# (5, 13) and (6, 12)
def small_trimino_problem():
    to_cover = [
        [1, 0, 0, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0],  # <- 5
        [1, 0, 0, 0, 0, 1, 1, 1],  # <- 6
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 0, 0],  # <- 12
        [0, 1, 0, 0, 0, 1, 1, 1],  # <- 13
    ]
    return dict(
        data=np.array(to_cover, dtype=DTYPE_FOR_ARRAY),
        solutions={(5, 13), (6, 12)},
    )


def small_trimino_problem_from_file():
    return dict(
        data=np.load("tests/data/small_trimino.npy"),
        solutions={(5, 13), (6, 12)},
    )


# https://en.wikipedia.org/wiki/Exact_cover#Detailed_example
def detailed_wikipedia_problem():
    sets = [
        {1, 4, 7},
        {1, 4},  # <- 1
        {4, 5, 7},
        {3, 5, 6},  # <- 3
        {2, 3, 6, 7},
        {2, 7},  # <- 5
    ]
    return dict(
        data=np.array(
            [[1 if i in s else 0 for i in range(1, 8)] for s in sets],
            dtype=DTYPE_FOR_ARRAY,
        ),
        solutions={(1, 3, 5)},
    )


def bruteforce_problem1():
    to_cover = [
        [1, 0, 0, 1, 0, 0, 1, 0],  # <- sol1
        [0, 1, 0, 0, 1, 0, 0, 1],  # <- sol1
        [0, 0, 1, 0, 0, 1, 0, 0],  # <- sol1
        [0, 0, 0, 1, 0, 0, 0, 0],  # <- sol2
        [1, 0, 1, 0, 1, 0, 0, 1],  # <- sol2
        [0, 1, 0, 0, 0, 1, 1, 0],  # <- sol2
    ]
    return dict(
        data=np.array(to_cover, dtype=DTYPE_FOR_ARRAY),
        solutions={(0, 1, 2), (3, 4, 5)}
    )


def bruteforce_problem2():
    to_cover = [
        [1, 0, 0, 1, 0, 0, 1, 0],  # <- sol1
        [0, 1, 0, 0, 1, 0, 0, 1],  # <- sol1
        [0, 0, 1, 0, 0, 1, 0, 0],  # <- sol1
        [0, 0, 0, 1, 0, 0, 0, 0],  # <- sol2
        [1, 0, 1, 0, 1, 0, 0, 1],  # <- sol2
        [0, 1, 0, 0, 0, 1, 1, 0],  # <- sol2
        [1, 0, 0, 1, 0, 0, 1, 0],  # <- sol1
        [0, 1, 0, 0, 1, 0, 0, 1],  # <- sol1
        [0, 0, 1, 0, 0, 1, 0, 0],  # <- sol1
    ]
    return dict(
        data=np.array(to_cover, dtype=DTYPE_FOR_ARRAY),
        solutions={
            (0, 1, 2),
            (0, 1, 8),
            (0, 7, 2),
            (0, 7, 8),
            (4, 5, 3),
            (6, 1, 2),
            (6, 1, 8),
            (6, 7, 2),
            (6, 7, 8),
        }
    )


def bruteforce_problem3():
    to_cover = [
        [1, 0, 0, 1, 0, 0, 1, 0],  # <- sol1
        [0, 1, 0, 0, 1, 0, 0, 1],  # <- sol1
        [0, 0, 1, 0, 0, 1, 0, 0],  # <- sol1
        [0, 0, 0, 1, 0, 0, 0, 0],  # <- sol2
        [1, 0, 1, 0, 1, 0, 0, 1],  # <- sol2
        [0, 1, 0, 0, 0, 1, 1, 0],  # <- sol2
        [1, 0, 0, 1, 0, 0, 1, 0],  # <- sol1
        [0, 1, 0, 0, 1, 0, 0, 1],  # <- sol1
        [0, 0, 1, 0, 0, 1, 0, 0],  # <- sol1
        [0, 0, 0, 1, 0, 0, 0, 0],  # <- sol2
        [1, 0, 1, 0, 1, 0, 0, 1],  # <- sol2
        [0, 1, 0, 0, 0, 1, 1, 0],  # <- sol2
    ]
    return dict(
        data=np.array(to_cover, dtype=DTYPE_FOR_ARRAY),
        solutions={
            (0, 1, 2),
            (0, 1, 8),
            (0, 7, 2),
            (0, 7, 8),
            (4, 5, 3),
            (4, 5, 9),
            (4, 11, 3),
            (4, 11, 9),
            (6, 1, 2),
            (6, 1, 8),
            (6, 7, 2),
            (6, 7, 8),
            (10, 5, 3),
            (10, 5, 9),
            (10, 11, 3),
            (10, 11, 9),
        }
    )

def knuth_original_problem():
    to_cover = np.array([
        [0, 0, 1, 0, 1, 1, 0],
        [1, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 1],
    ])
    return dict(
        data=to_cover,
        solutions={
            (0, 3, 4),
        }
    )

# not enabled for now
# def pentomino_5_12_problem():
def pentamino_5_12_unknownproblem():
    to_cover = pd.read_csv("tests/data/pentominos-5-12.csv").to_numpy()
    return dict(
        data=to_cover,
        solutions="UNTESTED",
    )

def pentomino_chessboard_unknownproblem():
    to_cover = pd.read_csv("tests/data/pentominos-chessboard.csv", sep=" ").to_numpy()
    return dict(
        data=to_cover,
        solutions="UNTESTED",
    )
