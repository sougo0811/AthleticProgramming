N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

B_expected = sum(B)/N
R_expected = sum(R)/N

print(B_expected+R_expected)