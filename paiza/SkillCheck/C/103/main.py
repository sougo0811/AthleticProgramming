N,M = map(int,input().split())
abM = [map(str, input().split()) for _ in range(M)]
aM, bM = [list(i) for i in zip(*abM)]

for i in range(1,N+1):
  print_list = []
  for j in range(M):
    if i%int(aM[j]) == 0:
      print_list.append(bM[j])
  if len(print_list) == 0:
    print(i)
  else:
    ans = " ".join(print_list)
    print(ans)
