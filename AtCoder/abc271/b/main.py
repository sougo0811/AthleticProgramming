N,Q = map(int,input().split())
LN = []
for i in range(N):
  ln = list(map(int,input().split()))
  LN.append(ln)
SQ, TQ = [], []
for _ in range(Q):
  s,t = map(int,input().split())
  SQ.append(s)
  TQ.append(t)
#print(LN)
for i in range(Q):
  print(LN[SQ[i]-1][TQ[i]])