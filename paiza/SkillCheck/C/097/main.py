N,X,Y = map(int,input().split())
for i in range(1,N+1):
    flg_A = False
    flg_B = False
    if i%X == 0:
        flg_A = True
    if i%Y == 0:
        flg_B = True
    if flg_A == True and flg_B == True:
        print("AB")
    elif flg_A == True and flg_B == False:
        print("A")
    elif flg_A == False and flg_B == True:
        print("B")
    else:
        print("N")