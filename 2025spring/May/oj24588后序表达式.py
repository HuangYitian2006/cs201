p='+-*/'
def cal(s):
    stk=[]
    ans=0.0
    s.reverse()
    while s:
        a=s.pop()
        if a in p:
            x2,x1=stk.pop(),stk.pop()
            if a == '+': stk.append(x1 + x2)
            if a == '-': stk.append(x1 - x2)
            if a == '*': stk.append(x1 * x2)
            if a == '/': stk.append(x1 / x2)
        else:
            stk.append(float(a))
    return stk[0]

for _ in range(int(input())):
    x=list(input().split())
    print(f'{cal(x):.2f}')
