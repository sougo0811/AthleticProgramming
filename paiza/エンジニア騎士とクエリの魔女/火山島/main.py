N = int(input())
S,M,L = map(int,input().split())
total = 0
for i in range(N):
  size = input()
  if size == "SS":
    total += S*0.5
  elif size == "S":
    total += S
  elif size == "M":
    total += M
  elif size == "L":
    total += L
  elif size == "LL":
    total += L*2
print(int(total))