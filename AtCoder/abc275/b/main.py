import sys
input = sys.stdin.readline

A,B,C,D,E,F = map(int,input().split())

ans = (A*B*C)-(D*E*F)
print(ans%998244353)