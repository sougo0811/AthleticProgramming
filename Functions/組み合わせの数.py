def cmb_normal(n,r):
  from operator import mul
  from functools import reduce
  r = min(n-r,r)
  if r == 0: return 1
  over = reduce(mul,range(n,n-r,-1))
  under = reduce(mul,range(1,r+1))
  return over//under

def cmb_numbig(n,r):
  if n-r < r: r = n-r
  if r == 0: return 1
  if r == 1: return n
  numerator = [n-r+k+1 for k in range(r)]
  denominator = [k+1 for k in range(r)]
  for p in range(2,r+1):
    pivot = denominator[p-1]
    if pivot > 1:
      offset = (n-r) % p
      for k in range(p-1,r,p):
        numerator[k-offset] /= pivot
        denominator[k] /= pivot
  result = 1
  for k in range(r):
    if numerator[k] > 1:
      result *= int(numerator[k])
  return result

if __name__ == "__main__":
  n,r = map(int,input().split())
  print(cmb_normal(n,r))
  print(cmb_numbig(n,r))