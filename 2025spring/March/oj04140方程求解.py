#f(x) = x3- 5x2+ 10x - 80 = 0
x=[0,1]
i=1
while abs(x[i]-x[i-1])>10**-9:
    f=x[i]**3-5*x[i]**2+10*x[i]-80
    k=3*x[i]**2-10*x[i]+10
    x.append(x[i]-f/k)
    i+=1
print(f'{x[-1]:.9f}')