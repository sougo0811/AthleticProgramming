S = list(input())
alf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
if len(S) == 8 and S[0] in alf and S[-1] in alf and S[1] != "0":
  s = S[1:7]
  s = "".join(s)
  try:
    s = int(s)
    print("Yes")
  except ValueError as e:
    print("No")
    exit()
else:
  print("No")

