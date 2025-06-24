p=[[] for i in range(10001)]
px=[1]*10001
px[1]=0
for i in range(2,10001):
    if px[i]:
        for j in range(i*2,10001,i):
            px[j]=0
#print(px)
for i in range(2,10001):
    if px[i] and i%10==1:
        for j in range(i,10001):
            p[j].append(i)
n=int(input())
for i in range(n):
    x=int(input())
    print(f'Case{i+1}:')
    if p[x-1]:
        print(*p[x-1])
    else:
        print('NULL')