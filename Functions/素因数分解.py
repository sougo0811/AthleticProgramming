def prime_factorization(n):
  import collections
  prime_factor = []
  for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
      prime_factor.append(i)
      n //= i
  if n != 1:
    prime_factor.append(n)
  return collections.Counter(prime_factor)

if __name__ == "__main__":
  n = int(input())
  prime_factor = prime_factorization(n)
  print(prime_factor)