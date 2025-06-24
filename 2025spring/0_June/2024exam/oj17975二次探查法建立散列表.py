import math
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
a = [int(i) for i in data[index:index+n]]
s=set()
nums=dict()
ans=[]
for i in range(n):
    if a[i] in nums:
        ans.append(nums[a[i]])
        continue
    x=a[i]%m
    fnum = 0
    while x in s:
        x=(a[i]%m+(-1)**(fnum+1)*(math.ceil(fnum/2))**2)%m
        fnum+=1
    ans.append(x)
    nums[a[i]]=x
    s.add(x)
print(*ans)