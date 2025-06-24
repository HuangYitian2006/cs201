class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=[]
        for i in s:
            '''print(i)
            if a:print(a[-1])'''
            if i in ['(','[','{']:
                a.append(i)
            elif (i,a[-1]) in ((')','('),(']','['),('}','{')):

                a.pop()
            else:
                return False
        return True
if __name__=='__main__':
    sol=Solution()
    print(sol.isValid('[}'))