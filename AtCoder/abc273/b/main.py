X,K = map(str,input().split())
X = list(map(int,X)); K = int(K)
X.reverse()


for i in range(K):
  if len(X) <= i:
    X = 0
    break
  else:
    if X[i] <= 4:
      X[i] = 0
    else:
      X[i] = 0
      if len(X) == i:
        X.append(1)
      else:
        if len(X) == i+1:
          X.append(0)
        X[i+1] += 1
        for j in range(len(X)):
          if X[j] >= 10:
            X[j] = 0
            if j+1 == len(X):
              X.append(0)
            X[j+1] += 1

if len(str(X)) > 1:
  X.reverse()
  if X[0] == 0:
    ans = 0
  else:
    ans = "".join(map(str,X))
else:
  ans = X
print(ans)