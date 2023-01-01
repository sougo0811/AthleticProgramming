m = int(input())

if m < 100:
  print("00")
elif m <= 5000:
  m = list(str(m))
  if len(m) == 3:
    print("0"+m[0])
  else:
    print(m[0]+m[1])
elif m <= 30000:
  m = m//1000+50
  print(m)
elif m <= 70000:
  m //= 1000
  m = (m-30)//5+80
  print(m)
else:
  print(89)