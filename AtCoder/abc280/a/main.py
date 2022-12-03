import sys
input = sys.stdin.readline

H,W = map(int,input().split())
S = []
cnt = 0
for _ in range(H):
  s = list(input())
  cnt += s.count("#")

print(cnt)