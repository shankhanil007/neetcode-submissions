class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1

        for idx in range(n-1, -1, -1):
            one_digit = s[idx]
            if 1 <= int(one_digit) <= 9:
                dp[idx] += dp[idx+1]
            
            if idx+1 < n:
                two_digit = s[idx: idx+2]
                if 10 <= int(two_digit) <= 26:
                    dp[idx] += dp[idx+2]


        return dp[0]