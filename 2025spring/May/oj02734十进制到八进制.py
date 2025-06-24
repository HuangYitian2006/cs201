n=int(input())
stk=[]
x=8
while n:
    stk.append(str(n%x))
    n//=x
stk.reverse()
print(''.join(stk))