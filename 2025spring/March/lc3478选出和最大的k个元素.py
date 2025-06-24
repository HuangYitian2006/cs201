import heapq
from heapq import heappush


class Solution:
    def findMaxSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        n=len(nums1)
        ans=[0]*n
        h=[]
        #先对数组按nums1排序，预处理
        a=sorted((x,y,i) for i,(x,y) in enumerate(zip(nums1,nums2)))
        s,i=0,0
        while i<n:
            start=i
            x=a[i][0]
            #先处理这些相等的nums1
            while i<n and a[i][0]==x:
                ans[a[i][2]]=s
                i+=1
            #再把他们对应的nums2值入堆
            for j in range(start,i):
                heapq.heappush(h,a[j][1])
                s+=a[j][1]
                if len(h)>k:
                    s-=heapq.heappop(h)
        return ans

if __name__ == '__main__':
    sol=Solution()
    print(sol.findMaxSum([4,2,1,5,3],[10,20,30,40,50],2))