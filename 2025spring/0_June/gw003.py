s=input()
stk=[]
flag1=1
flag2=0
for x in s:
    if x in {'(','[','{'}:
        stk.append(x)
        if len(stk)>1:flag2=1
    elif x in {')',']','}'}:
        if not stk or (stk[-1],x) not in {('(',')'),('[',']'),('{','}')}:
            flag1=0
            break
        else: stk.pop()
if stk: flag1=0
if flag1:
    if flag2:print('YES')
    else:print('NO')
else:print('ERROR')