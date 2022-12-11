N = int(input())

S = [i for i in range(2,N+1)]
n = 0; p = S[n]
while p <= N**0.5:
  S = [S[i] for i in range(len(S)) if S[i]%p != 0 or S[i] <= p]
  n += 1; p = S[n]
S = " ".join(map(str,S))
print(S)