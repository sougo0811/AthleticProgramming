M = int(input())
S = [i for i in range(2,M+1)]
n = 0; p = S[n]
while p <= M**0.5:
  S = [S[i] for i in range(len(S)) if S[i]%p != 0 or S[i] <= p]
  n += 1; p = S[n]

print(S); print(len(S))