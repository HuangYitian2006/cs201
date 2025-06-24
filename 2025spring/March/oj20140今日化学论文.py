s=input()
stk=[]
number= {'0','1','2','3','4','5','6','7','8','9'}
for i in range(len(s)):
    stk.append(s[i])
    if stk[-1]==']':
        hstk=[]
        stk.pop()
        while stk[-1]!='[':
            hstk.append(stk.pop())
        stk.pop()
        num=''
        while hstk[-1] in number:
            num+=hstk.pop()
        hstk*=int(num)
        while hstk:
            stk.append(hstk.pop())

print(*stk,sep='')