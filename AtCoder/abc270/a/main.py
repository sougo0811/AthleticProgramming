import sys
input = sys.stdin.readline

A,B = map(int,input().split())

#print(A|B) #bitのOR演算をすれば一発 

takahashi = {1:False,2:False,4:False}; aoki = {1:False,2:False,4:False}; sunuke = 0
if A == 1 or A == 2 or A == 4:
  takahashi[A] = True
elif A == 3 or A == 5:
  takahashi[1] = True; takahashi[A-1] = True
elif A == 6:
  takahashi[2] = True; takahashi[4] = True
elif A == 7:
  takahashi[1] = True; takahashi[2] = True; takahashi[4] = True

if B == 1 or B == 2 or B == 4:
  aoki[B] = True
elif B == 3 or B == 5:
  aoki[1] = True; aoki[B-1] = True
elif B == 6:
  aoki[2] = True; aoki[4] = True
elif A == 7:
  aoki[1] = True; aoki[2] = True; aoki[4] = True

if takahashi[1] or aoki[1]:
  sunuke += 1
if takahashi[2] or aoki[2]:
  sunuke += 2
if takahashi[4] or aoki[4]:
  sunuke += 4

print(sunuke)