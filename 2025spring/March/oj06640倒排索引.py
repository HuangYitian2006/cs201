n=int(input())
a=dict()
for i in range(n):
    c=input().split()
    for j in range(1,int(c[0])+1):
        if c[j] not in a:
            a[c[j]]=[i+1]
        elif a[c[j]][-1]!=(i+1):
            a[c[j]].append(i+1)
for i in range(int(input())):
    x=input()
    if x in a:
        print(*a[x])
    else:
        print('NOT FOUND')