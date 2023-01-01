Deg,Dis = map(float,input().split())
Dir,W = "N",0; Dis /=60
SC = 112.5
Degs = ["NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
for i in range(len(Degs)):
  if SC <= Deg < SC+225:
    Dir = Degs[i]
    break
  else:
    SC+=225


if 0.0 <= Dis <= 0.24:
  W = 0
  Dir = "C"
elif 0.25 <= Dis <= 1.54:
  W = 1
elif 1.55 <= Dis <= 3.34:
  W = 2
elif 3.35 <= Dis <= 5.44:
  W = 3
elif 5.45 <= Dis <= 7.94:
  W = 4
elif 7.95 <= Dis <= 10.74:
  W = 5
elif 10.75 <= Dis <= 13.84:
  W = 6
elif 13.85 <= Dis <= 17.14:
  W = 7
elif 17.15 <= Dis <= 20.74:
  W = 8
elif 20.75 <= Dis <= 24.44:
  W = 9
elif 24.45 <= Dis <= 28.44:
  W = 10
elif 28.45 <= Dis <= 32.64:
  W = 11
else:
  W = 12

print(Dir+" "+str(W))