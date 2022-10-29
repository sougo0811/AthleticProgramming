import sys
input = sys.stdin.readline

from functools import lru_cache

N = int(input())

#愚直に
@lru_cache(10**5)
def f(k):
  if k == 0:
    return 1
  else:
    return f(int(k/2)) + f(int(k/3))

print(f(N))