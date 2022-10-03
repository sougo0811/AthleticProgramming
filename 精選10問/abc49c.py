import sys
input = sys.stdin.readline
S = list(input());S.reverse(); S.pop(0)
words = ["maerd","remaerd","esare","resare"]
i = 0
for _ in range(len(S)):
  word = "".join(S[i:i+5])
  if word == words[0]:
    i += 5
    if len(S) == i:
      print("YES")
      break
    continue
  elif word == words[2]:
    i += 5
    if len(S) == i:
      print("YES")
      break
    continue
  word = "".join(S[i:i+6])
  if word == words[3]:
    i += 6
    if len(S) == i:
      print("YES")
      break
    continue
  word = "".join(S[i:i+7])
  if word == words[1]:
    i += 7
    if len(S) == i:
      print("YES")
      break
    continue
  else:
    print("NO")
    break