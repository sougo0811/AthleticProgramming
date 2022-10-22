import sys
input = sys.stdin.readline

A,B = map(int,input().split())

BA = B/A;ans = round(BA,3)

print('{:.3f}'.format(ans))