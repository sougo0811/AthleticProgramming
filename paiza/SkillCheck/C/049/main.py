N = int(input())
FN = []
for _ in range(N):
  f = int(input())
  FN.append(f)

ele = 1
long = 0
for i in range(N):
  long += abs(FN[i]-ele)
  ele = FN[i]
print(long)