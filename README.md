# exact cover in Python

an implementation of Donald Knuth's Dancing Links algorithm in pure Python

## Usage

```bash
pip install exact_cover_py
```

```python
from exact_cover_py import exact_cover

problem = np.array([
        [1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0],  # <--
        [0, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 0],  # <--
        [0, 1, 1, 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 1],  # <--
        [0, 1, 0, 0, 0, 0, 1],
   ])

# exact_cover returns a generator of solutions

# one solution
print(next(exact_cover(problem)))
[1, 5, 3]

# all solutions
print(list(exact_cover(problem)))
[[1, 5, 3]]
```

## Development

```bash
# install dependencies
pip install -e .[tests]

pytest
```
