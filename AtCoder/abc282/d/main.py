import sys
input = sys.stdin.readline

N,M = map(int,input().split())
u,v = [],[]
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)  # 有向グラフなら消す

print(G)