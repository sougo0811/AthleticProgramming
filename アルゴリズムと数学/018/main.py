N = int(input())
A = list(map(int,input().split()))

import collections
A_collection = collections.Counter(A)
print(A_collection[100]*A_collection[400]+A_collection[200]*A_collection[300])