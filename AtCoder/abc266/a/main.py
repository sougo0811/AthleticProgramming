import sys
input = sys.stdin.readline

S = list(input())
print(S[int(len(S)/2-1)]) #(-1で改行コード分の調整)