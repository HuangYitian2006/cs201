def check(m):
    s=0
    for x in score:
        if x*m/1e9+1.1**(x*m/1e9)>=85:
            s+=1
    if s>=student_number*0.6: return True
    else: return False
score=list(map(float,input().split()))
student_number=len(score)
l,r=0,1e9
while l<r-1:
    mid=(l+r)//2
    if check(mid): r=mid
    else: l=mid
print(int(r))