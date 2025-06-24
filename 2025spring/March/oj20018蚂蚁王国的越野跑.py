arr=[]
def mgsort(l,r):
    if l>=r:
        return 0
    mid=(l+r)//2
    cnt=mgsort(l,mid)+mgsort(mid+1,r)
    i,j,tmp=l,mid+1,[]
    while i<=mid and j<=r:
        if arr[i]<arr[j]:
            tmp.append(arr[j])
            cnt+=mid-i+1
            j+=1
        else:
            tmp.append(arr[i])
            i+=1
    while i<=mid:
        tmp.append(arr[i])
        i+=1
    while j<=r:
        tmp.append(arr[j])
        j+=1
    arr[l:r+1]=tmp
    #print(l,r,arr,cnt)
    return cnt
n=int(input())
for i in range(n):
    arr.append(int(input()))
print(mgsort(0,n-1))