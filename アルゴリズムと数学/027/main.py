N = int(input())
A = list(map(int, input().split()))

def merge_sort(A):
  if len(A) == 1:
    return A
  m = len(A)//2
  A_Dash = merge_sort(A[0:m])
  B_Dash = merge_sort(A[m:len(A)])

  c1 = 0; c2 = 0; C = []
  while c1 < len(A_Dash) and c2 < len(B_Dash):
    if c1 == len(A_Dash):
      C.append(B_Dash[c2])
      c2 += 1
    elif c2 == len(B_Dash):
      C.append(A_Dash[c1])
      c1 += 1
    else:
      if A_Dash[c1] < B_Dash[c2]:
        C.append(A_Dash[c1])
        c1 += 1
      else:
        C.append(B_Dash[c2])
        c2 += 1
  C += A_Dash[c1:]; C += B_Dash[c2:]
  return C

print(*(merge_sort(A)))