n,r = map(int,input().split())

from math import factorial
print(factorial(n) // factorial(r) // factorial(n - r))