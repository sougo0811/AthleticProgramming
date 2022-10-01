N = int(input())
N16 = hex(N)
if len(N16) == 4:
  print(N16[2:].upper())
else:
  print("0"+N16[2:].upper())