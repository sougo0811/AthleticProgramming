import sys
input = sys.stdin.readline
N = int(input())
aN = list(map(int, input().split()))
aN.sort(reverse=True)
Alice = 0; Bob = 0
for i in range(N):
  if i%2 == 0:
    Alice += aN[i]
  else:
    Bob += aN[i]
print(Alice - Bob)