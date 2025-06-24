class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            ans.append([1] + [ans[i - 1][j] + ans[i - 1][j + 1] for j in range(i - 1)] + [1])
        return ans

if __name__=='__main__':
    sol=Solution()
    print(sol.generate(5))