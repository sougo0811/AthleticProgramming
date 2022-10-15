import sys
input = sys.stdin.readline

N = int(input())
AN = list(map(int,input().split()))

odd_count = 0; even_cnt = 0; max_1 = 0; max_2 = 0; max_3 = 0; max_4 = 0
for i in range(N):
  if AN[i]%2 == 0:
    even_cnt += 1
    max_2 = max(max_2,AN[i])
    if max_1 < max_2:
      max_1,max_2 = max_2,max_1
  else:
    odd_count += 1
    max_4 = max(max_4,AN[i])
    if max_3 < max_4:
      max_3,max_4 = max_4,max_3
if even_cnt < 2 and odd_count < 2:
  print(-1)
else:
  if max_1 + max_2 >= max_3 + max_4:
    print(max_1 + max_2)
  else:
    print(max_3 + max_4)