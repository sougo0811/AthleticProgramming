N = int(input())
x_R,x_G,x_B = map(int,input().split())
t_N = []
c_N = []
for _ in range(N):
  t,c = map(str,input().split())
  t_N.append(t)
  c_N.append(c)

flg = True

for i in range(N):
  if t_N[i] == "R":
    if c_N[i] == "R":
      x_R += 1
    elif c_N[i] == "G":
      x_G += 1
    elif c_N[i] == "B":
      x_B += 1
    elif c_N[i] == "Y":
      x_R += 1
      x_G += 1
    elif c_N[i] == "M":
      x_R += 1
      x_B += 1
    elif c_N[i] == "C":
      x_B += 1
      x_G += 1
    else:
      x_R += 1
      x_B += 1
      x_G += 1
  else:
    if c_N[i] == "R":
      x_R -= 1
    elif c_N[i] == "G":
      x_G -= 1
    elif c_N[i] == "B":
      x_B -= 1
    elif c_N[i] == "Y":
      x_R -= 1
      x_G -= 1
    elif c_N[i] == "M":
      x_R -= 1
      x_B -= 1
    elif c_N[i] == "C":
      x_B -= 1
      x_G -= 1
    else:
      x_R -= 1
      x_B -= 1
      x_G -= 1
  if x_R == x_B == x_G:
    print(x_R)
    flg = False
    break
if flg:
  print("no")