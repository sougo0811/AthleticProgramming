import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

cnt = 0
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      for l in range(k+1,N):
        for m in range(l+1,N):
          if A[i]+A[j]+A[k]+A[l]+A[m] == 1000:
            cnt += 1
print(cnt)