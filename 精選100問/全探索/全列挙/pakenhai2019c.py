import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ANM = []
for _ in range(N):
  AM = list(map(int,input().split()))
  ANM.append(AM)
#print(ANM)
ans = 0; score = [0]*N
for i in range(M-1):
  for j in range(i+1,M):
    for k in range(N):
      score[k] = max(ANM[k][i],ANM[k][j])
    ans = max(ans, sum(score))
print(ans)
