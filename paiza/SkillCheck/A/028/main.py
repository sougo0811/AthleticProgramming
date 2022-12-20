S,P = map(int,input().split())

while P > 0:
  flg = True
  for i in range(1,P+1):
    if S*i//100 >= 1:
      flg = False
      S = int(S*(100+i)/100)
      P -= i
      break
  if flg:
    P -= 1
    S = int(S*(100+1)/100)
print(S)