S = input()
S_l = list(S)
S_lc = list(S_l)

b = ["a","A","i","I","u","U","e","E","o","O"]
cnt = 0
for i in range(len(S_l)):
  if S_lc[i] in b:
    S_l.pop(i-cnt)
    cnt += 1
S_s = "".join(S_l)
print(S_s)