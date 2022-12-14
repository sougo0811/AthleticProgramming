N = int(input())
A = list(map(int,input().split()))
a = A[0]
for i in range(1,N):
  b = A[i]
  while(a >= 1 and b >= 1):
    if a > b:
      a %= b
    else:
      b %= a
  if a == 0:
    a = b
print(a)