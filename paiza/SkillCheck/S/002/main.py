from collections import deque

N,M = map(int,input().split())
S = []
wall = ["1" for i in range(N+2)]
for i in range(M):
  s = list(map(str,input().split()))
  if "s" in s:
    sx = s.index("s") + 1
    sy = i + 1
  if "g" in s:
    gx = s.index("g") + 1
    gy = i + 1
  s.insert(0,"1")
  S.append(s)
  s.append("1")
S.insert(0,wall)
S.append(wall)
#print(S)

r = N+2
c = M+2
def find_shortest():
  d = [[float("inf")] * r for i in range(c)]
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  que = deque([])
  que.append((sy,sx))
  d[sy][sx] = 0

  while que:
    p = que.popleft()
    if p[0] == gy and p[1] == gx:
      break
    for i in range(4):
      nx = p[0] + dx[i]
      ny = p[1] + dy[i]

      if 0 <= nx < c and 0 <= ny < r and S[nx][ny] != "1" and d[nx][ny] == float("inf"):
        que.append((nx, ny))
        d[nx][ny] = (d[p[0]][p[1]] + 1)
  return d[gy][gx]

ans = find_shortest()
if ans == float("inf"):
  print("Fail")
else:
  print(ans)