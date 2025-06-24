import math

a,b,c,d=map(int,input().split())
x=a*d+b*c
y=b*d
g=math.gcd(x,y)
print(f'{x//g}/{y//g}')