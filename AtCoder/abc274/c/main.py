import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
ameba = [0]*(2*N+1)

for i,a in enumerate(A):
  #print(i,a)
  ameba[2*i+1] = ameba[a-1]+1
  ameba[2*i+2] = ameba[a-1]+1

for j in range(2*N+1):
  print(ameba[j])
'''
import sys
input = sys.stdin.readline
from collections import defaultdict
d = defaultdict(dict)

def get_key(d, val_search):
    keys = [key for key, value in d.items() if val_search in value]
    if keys :
        return keys[0]
    else :
        return None

N = int(input())
A = list(map(int,input().split()))
ameba = {str(i):[] for i in range(2**N)}
ameba['0'] = [1]

for i in range(1,N+1):
  k = str(int(get_key(ameba,A[i-1]))+1)
  ameba[k].append(2*i)
  ameba[k].append(2*i+1)
#print(ameba)

for j in range(1,2*N+2):
  k = int(get_key(ameba,j))
  print(k)

'''
