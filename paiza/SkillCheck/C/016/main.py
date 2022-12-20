s = input()
sl = list(s)

for i in range(len(sl)):
  if sl[i] == "A":
    sl[i] = "4"
  elif sl[i] == "E":
    sl[i] = "3"
  elif sl[i] == "G":
    sl[i] = "6"
  elif sl[i] == "I":
    sl[i] = "1"
  elif sl[i] == "O":
    sl[i] = "0"
  elif sl[i] == "S":
    sl[i] = "5"
  elif sl[i] == "Z":
    sl[i] = "2"

sl = "".join(sl)
print(sl)