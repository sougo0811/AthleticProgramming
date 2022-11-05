import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))
Pr = list(reversed(P))

Q = [Pr[0]]; Pr.pop(0)

for i in range(1,N):
  if Pr[0] < Q[-1]:
    Q.append(Pr[0])
    Pr.pop(0)
  else:
    q = Pr[0]
    Q.append(Pr[0])
    Pr.pop(0)
    Qs = sorted(Q)
    qi = Qs.index(q)
    if qi != 0:
      Pr = list(reversed(Pr))
      Pr.append(Qs[qi-1])
      Qs.pop(qi-1)
      Qr = list(reversed(Qs))
      Pr.extend(Qr)
      P = " ".join(map(str,Pr))
      print(P)
      exit()