N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sum = sum(A)
B_sum = sum(B)

ans = (A_sum)/3 + 2*(B_sum)/3
print(ans)