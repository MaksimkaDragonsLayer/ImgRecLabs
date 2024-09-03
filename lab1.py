import numpy as np
rng = np.random.default_rng()

a = rng. integers(-10, 10, (3, 2, 5))
print(a)
c = np.copy(a)

"""
[[[ -5   4  -3  -5   9]
  [  9  -6   2   0  -8]]

 [[  6   7  -7  -9  -5]
  [ -6  -3  -8  -6   2]]

 [[ -7  -2  -3 -10  -7]
  [  1   3   8   6   7]]]
"""

b = rng. integers(-10, 10, (3, 2, 5))
print(b)

"""
[[[  2   7   9  -4   2]
  [  9  -6  -4  -9   4]]

 [[ -6   4  -7   2   6]
  [ -4  -7 -10   0 -10]]

 [[-10  -8 -10   0  -8]
  [ -9  -5   7   4   5]]]
"""

print(np.equal(a, b))

"""
[[[False False False False False]
  [ True  True False False False]]

 [[False False  True False False]
  [False False False False False]]

 [[False False False False False]
  [False False False False False]]]
"""

print(np.equal(a, c))

"""
[[[ True  True  True  True  True]
  [ True  True  True  True  True]]

 [[ True  True  True  True  True]
  [ True  True  True  True  True]]

 [[ True  True  True  True  True]
  [ True  True  True  True  True]]]
"""