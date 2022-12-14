def gcd_two(A,B):
  if A < B:
    A,B = B,A
  while B > 0:
    A,B = B,A%B
  return A

def lcd_two(A,B):
  return A*B//gcd_two(A,B)

if __name__ == "__main__":
  A,B = map(int,input().split())
  print(gcd_two(A,B))
  print(lcd_two(A,B))