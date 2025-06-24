opr={'+','-','*','/'}
precedence={'+':1,'-':1,'*':2,'/':2}
def cal(s):
    stk=[]
    postfix=[]
    ans=[]
    number=''
    for x in s:
        if x.isnumeric() or x=='.':
            number+=x
        else:
            if number:
                postfix.append(number)
                number=''
            if x in opr:
                while stk and stk[-1] in opr and \
                        precedence[x]<=precedence[stk[-1]]:#只要不是后面的更优先，都先算前面的
                    postfix.append(stk.pop())
                stk.append(x)
            elif x=='(':
                stk.append(x)
            elif x==')':
                while stk and stk[-1]!='(':
                    postfix.append(stk.pop())
                stk.pop()
    if number:
        postfix.append(number)
    while stk:
        postfix.append(stk.pop())
    return ' '.join(postfix)



for _ in range(int(input())):
    s=input()
    print(cal(s))
