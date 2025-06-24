from functools import cmp_to_key
def cmp(x,y):
    if x[0]<y[0]: return -1
    elif x[0]>y[0]: return 1
    if x[1][-1]>y[1][-1]: return -1
    elif x[1][-1]<y[1][-1]: return 1
    if float(x[1][:-1])<float(y[1][:-1]): return -1
    else: return 1
n=int(input())
a=[]
for i in range(n):
    a.append(input().split('-'))
a.sort(key=cmp_to_key(cmp))
cur=''
for i in range(n):
    if a[i][0]==cur:
        print(f', {a[i][1]}',end='')
    else:
        if i!=0:print()
        print(f'{a[i][0]}: {a[i][1]}',end='')
        cur=a[i][0]
