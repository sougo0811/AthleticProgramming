N = int(input())
P = []; Q = []
for _ in range(N):
    p, q = map(int, input().split())
    P.append(p); Q.append(q)

expected_value = 0

for i in range(N):
  expected_value += Q[i]/P[i]

print(expected_value)