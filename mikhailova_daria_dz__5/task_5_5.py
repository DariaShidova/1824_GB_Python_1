import sys
from time import perf_counter
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 7, 87, 90, 56, 8, 11]

r = (el for el in src if src.count(el) == 1)
print(type(r), sys.getsizeof(r), perf_counter())
print(list(r))

