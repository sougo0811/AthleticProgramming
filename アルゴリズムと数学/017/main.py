N = int(input())
A = list(map(int,input().split()))

lcd = A[0]; gcd = A[0]
for i in range(1,N):
  a = A[i]
  if gcd < a:
    gcd,a = a,gcd
  while a > 0:
    gcd,a = a,gcd%a
  lcd = lcd*A[i]//gcd
  gcd = lcd

print(lcd)