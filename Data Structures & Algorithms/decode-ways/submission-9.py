class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        memo = {}

        def helper(idx):
            if idx >= n:
                return 1
            
            if idx in memo:
                return memo[idx]

            curr = 0

            one_digit = s[idx]
            if 1 <= int(one_digit) <= 9:
                curr += helper(idx+1)
            
            two_digit = s[idx: idx+2]
            if 10 <= int(two_digit) <= 26:
                curr += helper(idx+2)

            memo[idx] = curr
            return memo[idx]

        return helper(0)