H,W,X = map(int,input().split())
s_HW = []

for _ in range(H):
  s_W = list(map(int,input().split()))
  s_HW.append(s_W)

pt = 0
pin = []
pin_add = []
pin.append(X)
for i in range(H):
  for j in (pin):
    pt += s_HW[i][j-1]
    if j-1 > 0:
      pin_add.append(j-1)
    if j+1 <= W:
      pin_add.append(j+1)
  pin.extend(pin_add)
  pin = list(set(pin))

print(pt)