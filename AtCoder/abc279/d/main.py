import sys
input = sys.stdin.readline

A,B = map(int,input().split())
min_x = ((A/(2*B))**(2/3))-1
def f(n):
  return B*n + A/((n+1)**(1/2))

if min_x >= (A/B):
  print(f(0))
else:
  ans_li = [i+int(min_x) for i in range(-5,5) if i+int(min_x) >= 0]
  ans = f(int(min_x))
  for i in range(len(ans_li)):
    ans = min(ans,f(ans_li[i]))
  print(ans)