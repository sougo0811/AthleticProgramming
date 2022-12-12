N = int(input())
A = []
for i in range(1,int(N**0.5)+1):
  if N%i == 0:
    A.append(i)
    A.append(N//i)
A = set(A)
for i in A:
  print(i)