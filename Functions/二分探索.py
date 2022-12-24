def binary_search(N,A,X):
  min = 0; max = N - 1
  while min <= max:
    mid = (min + max) // 2
    if A[mid] == X:
      return "Yes" #midが位置
    elif A[mid] < X:
      min = mid + 1
    else:
      max = mid - 1
  return "No"

if __name__ == "__main__":
  N,X = map(int,input().split())
  A = list(map(int,input().split()))
  A = sorted(A)
  print(binary_search(N,A,X))

#bisect
import bisect
bisect.bisect(A,N) #Aの中でNより大きい最初の要素の位置を返す
bisect.bisect_left(A,N) #Aの中でN以上の最初の要素の位置を返す
bisect.bisect_right(A,N) #Aの中でNより大きい最初の要素の位置を返す
bisect.insort(A,N) #Aの中でNより大きい最初の要素の位置にNを挿入する