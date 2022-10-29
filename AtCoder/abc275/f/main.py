import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))

def get_integral_value_combination(list, target):
    def a(idx, l, r, t):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(list)):
            a((u + 1), l + [list[u]], r, t)
        return r
    return a(0, [], [], target)

for x in range(1,M+1):
  ans = get_integral_value_combination(A, x)
  print(ans)