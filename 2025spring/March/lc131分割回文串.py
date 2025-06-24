def partition(s: str) -> list[list[str]]:
    def check(a):
        if len(a) in (0,1):
            return True
        l, r = 0, len(a) - 1
        while l <= r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True

    dp = [[] for i in range(len(s) + 1)]
    dp[0]=[[]]
    dp[1]=[[s[0]]]
    #print(dp)
    for i in range(2,len(s)+1):
        for j in range(i):
            if check(s[j:i]):
                dp[i].extend([x+[s[j:i]] for x in dp[j]])
        #print(dp[i])
    #print(dp)
    return dp[len(s)]
print(partition('abb'))