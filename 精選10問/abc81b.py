import sys
input = sys.stdin.readline
N = int(input())
AN = list(map(int,input().split()))
cnt = 0
while True:
  for i in range(N):
    if AN[i]%2 != 0:
      break
  else:
    for j in range(N):
      AN[j] /= 2
    cnt += 1
    continue
  break

print(cnt)