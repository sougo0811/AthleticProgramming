import sys
input = sys.stdin.readline

A,B = map(int,input().split())
min_x = ((A/2*B)**(2/3))-1
def f(n):
  global A,B
  return B*n + A*((n+1)**-0.5)

if min_x >= (A/B):
  print(f(0))
else:
  ans_li = [i+int(min_x) for i in range(-2,3) if i+int(min_x) >= 0] 
  ans = f(int(min_x))
  for i in range(4):
    ans = min(ans,f(ans_li[i]))
  print(ans)