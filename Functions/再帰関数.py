def factorial(N):
  if N == 1:
    return 1
  else:
    return N * factorial(N-1)

def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a%b)