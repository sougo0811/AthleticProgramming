def irreducible_enumeration(n):
  irreducible = []
  cnt = 1
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      if i == n // i:
        irreducible.insert(cnt-1,i)
        cnt += 1
        continue
      irreducible.insert(cnt-1,n//i)
      irreducible.insert(-cnt,i)
      cnt += 1
  return irreducible

if __name__ == "__main__":
  n = int(input())
  print(irreducible_enumeration(n))