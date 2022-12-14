def gcd_N(N,*A):
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
  return a

def gcd(a,b):
  if a < b:
    a,b = b,a
  while b > 0:
    a,b = b,a%b
  return a

def lcd_N(N,*A):
  lcd = A[0]
  for i in range(1,N):
    lcd = lcd*A[i]//gcd(lcd,A[i])
  return lcd

if __name__ == "__main__":
  N = int(input())
  A = list(map(int,input().split()))
  print(gcd_N(N,*A))
  print(lcd_N(N,*A))