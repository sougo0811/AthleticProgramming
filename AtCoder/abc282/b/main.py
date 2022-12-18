import sys
input = sys.stdin.readline

N,M = map(int,input().split())
S = []
for _ in range(N):
    S.append(input().rstrip())

cnt = 0
for i in range(N):
  for j in range(i+1,N):
    if all([i in "o" for i in S[i]]):
      cnt += 1
    else:
      ans = 0
      for k in range(M):
        if S[i][k] == "o" or S[j][k] == "o":
          ans += 1
      if ans == M:
        cnt += 1
print(cnt)