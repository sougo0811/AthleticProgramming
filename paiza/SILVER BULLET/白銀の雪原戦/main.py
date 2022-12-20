import itertools

N = int(input())
aN = []
for _ in range(N):
  a = list(map(int,input().split()))
  aN.append(a)

ans = []
for i in range(N):
  A = list(itertools.permutations(aN[i], 6))
  MS = 0
  for j in range(len(A)):
    xs = []
    ys = []
    x_1 = A[j][0]
    y_1 = A[j][1]
    x_2 = A[j][2]
    y_2 = A[j][3]
    x_3 = A[j][4]
    y_3 = A[j][5]
    xs = [abs(x_1 - x_2),abs(x_2 - x_3),abs(x_3 - x_1)]
    ys = [abs(y_1 - y_2),abs(y_2 - y_3),abs(y_3 - y_1)]
    a = ((xs[0]**2)+(ys[0]**2))**0.5
    b = ((xs[1]**2)+(ys[1]**2))**0.5
    c = ((xs[2]**2)+(ys[2]**2))**0.5
    s =(a+b+c)*0.5
    if s-a < 0 or s-b < 0 or s-c < 0:
      S = 0
    else:
      S = (s*(s-a)*(s-b)*(s-c))**0.5
    if MS < S:
      MS = S
  ans.append(int(MS))
#print(ans)
print(ans.index(max(ans))+1)
