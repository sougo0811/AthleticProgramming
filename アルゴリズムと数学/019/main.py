N = int(input())
A = list(map(int,input().split()))

one = A.count(1)*(A.count(1)-1)/2
two = A.count(2)*(A.count(2)-1)/2
three = A.count(3)*(A.count(3)-1)/2
one = 0 if one < 0 else one
two = 0 if two < 0 else two
three = 0 if three < 0 else three
print(int(one+two+three))