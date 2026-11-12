class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [0] * (n+1)

        dp[0] = 1

        for i in range(1, n+1):
            one_digit = s[i-1:i]
            if 1<= int(one_digit) <= 9:
                dp[i] += dp[i-1]
            if i>1:
                two_digit = s[i-2:i]
                if 10 <= int(two_digit) <= 26:
                    dp[i] += dp[i-2]

        return dp[n]