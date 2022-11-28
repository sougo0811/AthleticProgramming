import sys
input = sys.stdin.readline

H,M = map(int,input().split())

while True:
  h1 = H//10; h2 = H%10
  m1 = M//10; m2 = M%10
  if h1 == 2:
    if m1 <= 3:
      print(str(H)+" "+str(M))
      break
  if h1 <= 1:
    if h2 <= 5:
      print(str(H)+" "+str(M))
      break
  if M == 59:
    M = 0
    if H == 23:
      H = 0
    else:
      H += 1
  else:
    M += 1
