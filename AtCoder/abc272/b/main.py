import sys
input = sys.stdin.readline

N,M = map(int,input().split())
km = []
for _ in range(M):
  m = list(map(int,input().split()))
  km.append(m[1::])

import itertools

all = itertools.combinations(range(1,N+1),2)
ans = []
for i in all:
  ans.append(list(i))

for i in range(M):
  delist = []
  for j in (ans):
    if set(j) <= set(km[i]):
      delist.append(j)
  new_ans = [i for i in ans if i not in delist]
  ans = new_ans; new_ans = []
  if len(ans) == 0:
    print("Yes")
    break
#print(ans)
if len(ans) != 0:
  print("No")