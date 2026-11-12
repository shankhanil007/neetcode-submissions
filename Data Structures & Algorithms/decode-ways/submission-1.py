class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [0] * (n+1)
        
        # Base cases
        dp[0] = 1
        if 1 <= int(s[0]) <= 9:
            dp[1] = 1

        for i in range(2, n+1):
            # Check 1-digit decoding (s[i-1])
            one_digit = int(s[i-1: i])
            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]

            # Check 2-digit decoding (s[i-2:i])
            two_digits = int(s[i - 2 : i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]