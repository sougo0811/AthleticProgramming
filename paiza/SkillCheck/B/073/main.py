import math
N,M = map(int,input().split())
AN = list(map(int,input().split()))
Q = int(input())
SEQ = [map(int, input().split()) for _ in range(Q)]
SQ, EQ = [list(i) for i in zip(*SEQ)]

for j in range(Q):
  start = SQ[j]
  end = EQ[j]
  total = 0
  put = 0
  for k in range(start,end+1):
    total += AN[k-1]
  ave = total/(end-start+1)
  if ave < M:
    put = M-math.floor(ave)
  for i in range(start,end+1):
    AN[i] += put

AN = " ".join(list(map(str,AN)))
print(AN)