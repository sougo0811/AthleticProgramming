N,M= map(int,input().split())
AM = []
for _ in range(M):
    am = int(input())
    AM.append(am)
HMN = []
for i in range(N):
    HM = []
    for j in range(M):
        hm = int(input())
        HM.append(hm)
    HMN.append(HM)
points = []
for i in range(N):
    point = 100
    for j in range(M):
        if AM[j] - 5 <= HMN[i][j] <= AM[j] + 5:
            point -= 0
        elif AM[j] - 10 <= HMN[i][j] <= AM[j] + 10:
            point -= 1
        elif AM[j] - 20 <= HMN[i][j] <= AM[j] + 20:
            point -= 2
        elif AM[j] - 30 <= HMN[i][j] <= AM[j] + 30:
            point -= 3
        else:
            point -= 5
    if point < 0:
        point = 0
    points.append(point)
points = sorted(points)
max_point = points[-1]
print(max_point)