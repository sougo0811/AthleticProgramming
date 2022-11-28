import sys
input = sys.stdin.readline

N,M = map(int,input().split())
AB = []
for _ in range(M):
  a,b = map(int,input().split())
  ab = [a,b]
  ba = [b,a]
  AB.append(ab); AB.append(ba)

ABsort = sorted(AB)

ans = [[] for _ in range(N+1)]
for i in range(2*M):
  ans[ABsort[i][0]].append(ABsort[i][1])

for j in range(1,N+1):
  ans_num = len(ans[j])
  ans_j = " ".join(map(str,ans[j]))
  print(str(len(ans[j]))+ " " + ans_j)


#TEL
'''
ABsort = sorted(AB)
#print(ABsort)
ans = []
for i in range(1,N+1):
  for j in range(M):
    if ABsort[j][0] == i:
      ans.append(ABsort[j][1])
    if ABsort[j][1] == i:
      ans.append(ABsort[j][0])
  ans_num = len(ans)
  ans = " ".join(map(str,ans))
  print(str(ans_num) + " " + ans)
  ans = []
'''