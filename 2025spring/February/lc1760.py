import math


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def check(m):
            s=0
            for i in nums:
                s+=math.ceil(i/m)-1
            return s<=maxOperations
        left, right = 0, max(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumSize([9], 2))
