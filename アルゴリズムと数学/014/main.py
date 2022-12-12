N = int(input())

def pfd(n):
  A = []
  for i in range(2,int(n**0.5)+1):
    while n%i == 0:
      A.append(i)
      n = n//i
  if n != 1:
    A.append(n)
  return A
ans = pfd(N); ans = " ".join(map(str,ans))
print(ans)