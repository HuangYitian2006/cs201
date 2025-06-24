n=int(input())
a=list(map(int,input().split()))
stk=[]
for i in range(n):
    while stk and a[stk[-1]]<a[i]:
        a[stk.pop()]=i+1
    stk.append(i)
while stk:
    a[stk.pop()]=0
print(*a)