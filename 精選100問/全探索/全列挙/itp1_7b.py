import itertools
import sys
input = sys.stdin.readline
while True:
  n,x = map(int,input().split())
  if (n,x) == (0,0):
    break
  all = [i for i in range(1,n+1)]
  all = itertools.combinations(all,3)
  cnt = 0
  for i in all:
    #print(i)
    if sum(i) == x:
      cnt += 1
  print(cnt)