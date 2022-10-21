import sys
input = sys.stdin.readline

N = int(input())
AN = list(map(int,input().split()))

odd_count = 0; even_cnt = 0; even_max_1 = 0; even_max_2 = 0; odd_max_1 = 0; odd_max_2 = 0
for i in range(N):
  if AN[i]%2 == 0:
    even_cnt += 1
    even_max_2 = max(even_max_2,AN[i])
    if even_max_1 < even_max_2:
      even_max_1,even_max_2 = even_max_2,even_max_1
  else:
    odd_count += 1
    odd_max_2 = max(odd_max_2,AN[i])
    if odd_max_1 < odd_max_2:
      odd_max_1,odd_max_2 = odd_max_2,odd_max_1
if even_cnt < 2 and odd_count < 2:
  print(-1)
else:
  if even_max_1 + even_max_2 >= odd_max_1 + odd_max_2:
    print(even_max_1 + even_max_2)
  else:
    print(odd_max_1 + odd_max_2)