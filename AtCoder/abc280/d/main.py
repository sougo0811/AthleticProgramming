import sys
input = sys.stdin.readline

K = int(input())

#素因数分解
def factorization(n):
  arr = []
  temp = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if temp%i==0:
      cnt=0
      while temp%i==0:
        cnt+=1
        temp //= i
      arr.append([i, cnt])
  if temp!=1:
    arr.append([temp, 1])
  if arr==[]:
    arr.append([n, 1])
  return arr

prime_factor = factorization(K)

#print(prime_factor)

#裏解法
'''
def gcd(a,b):
  if a < b:
    a,b = b,a
  while b > 0:
    a,b = b,a%b
  return a

for j in range(1,2*(10**6)):
  K/=gcd(K,j)
  if K == 1:
    print(j)
    exit()
print(int(K))
'''

#WA
'''
for i in range(len(prime_factor)):
  if (K**0.5) <= prime_factor[i][0]:
    print(K)
    exit()

for i in range(2,int(K**0.5)+1):
  n = factorization(i)
  for j in range(len(prime_factor)):
    for k in range(len(n)):
      if prime_factor[j][0] == n[k][0]:
        prime_factor[j][1] -= n[k][1]
        break
  if prime_factor[j][1] <= 0:
    print(i)
    exit()
'''

#TEL
'''
if len(prime_factor) == 1 and prime_factor[0][1] == 1:
  print(prime_factor[0][0])
  exit()

n = {}

from collections import Counter

def merge_dict(d1, d2):
    c1 = Counter(d1)
    c2 = Counter(d2)
    return dict(c1 + c2)

def compare_dict(d1, d2):
    for k in range(len(d2)):
      if d1.get(d2[k][0]) == None:
        return False
      if d1[d2[k][0]] - d2[k][1] < 0:
        return False
    return True

for i in range(2,K):
  a = factorization(i)
  b = dict(a)
  n = merge_dict(n,b)
  if compare_dict(n,prime_factor):
    print(i)
    break
'''

