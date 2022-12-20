m,p,q = map(int,input().split())

sold = 0
sold += m*(p/100)
sold += (m-sold)*(q/100)
print(m-sold)
