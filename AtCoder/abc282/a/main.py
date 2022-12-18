import sys
input = sys.stdin.readline

K = int(input())
alf = ["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ans = alf[:K]
ans = "".join(ans)
print(ans)