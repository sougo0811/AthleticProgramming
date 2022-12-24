import sys
input = sys.stdin.readline

S = input().rstrip()
cnt = 0
X = [set() for _ in range(len(S))]

for i in range(len(S)):
  if S[i] == "(":
    cnt += 1
    X[cnt] = set(X[cnt-1])
  elif S[i] == ")":
    X[cnt] = set()
    cnt -= 1
  else:
    if S[i] in X[cnt]:
      print("No")
      exit()
    X[cnt] = set(X[cnt]) | set([S[i]])

print("Yes")