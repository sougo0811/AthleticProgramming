import sys
input = sys.stdin.readline
N,A,B = map(int,input().split())

def digitSum(n):
  s = str(n)
  array = list(map(int,s))
  return sum(array)

total = 0
for i in range(1,N+1):
  if A <= digitSum(i) <= B:
    total += i

print(total)