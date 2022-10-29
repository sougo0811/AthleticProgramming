import sys
input = sys.stdin.readline

N = int(input())
HN = list(map(int, input().split()))

print(HN.index(max(HN))+1)