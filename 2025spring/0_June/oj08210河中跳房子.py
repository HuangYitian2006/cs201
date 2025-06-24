from xml.sax.saxutils import escape

l,n,m=0,0,0
def check(x): #x为可能的最小间距
    num=0
    now=0
    for i in range(1,n+2):
        if d[i]-now<x:
            num+=1
        else:
            now=d[i]
    if num>m:return False
    else: return True
l,n,m=map(int,input().split())
d=[0]
for i in range(n):
    d.append(int(input()))
d.append(l)
left,right=1,l+1
while left<right-1:
    mid=(left+right)//2
    if check(mid):
        left=mid
    else:right=mid
print(left)