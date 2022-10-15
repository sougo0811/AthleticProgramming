import sys
input = sys.stdin.readline

N = int(input())
AN = list(map(int,input().split()))
BN = sorted(list(set(AN)))

import bisect

anslist = []
for i in range(N):
  a = bisect.bisect(BN,AN[i])
  cnt = len(BN) - a
  anslist.append(cnt)

import collections
c = collections.Counter(anslist)
for i in range(N):
  print(c[i])

'''
anslist = []
for i in range(N):
  ans = sum(j > AN[i] for j in set(AN))
  anslist.append(ans)

import collections
c = collections.Counter(anslist)
for i in range(N):
  print(c[i])
'''