class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        memo = {}

        def helper(idx):
            if idx >= n:
                return 1

            state = idx
            if state in memo:
                return memo[state]
            
            ways = 0
            one_digit = s[idx]
            if 1<= int(one_digit) <= 9:
                ways += helper(idx+1)
            if idx < n-1:
                two_digit = s[idx:idx+2]
                if 10 <= int(two_digit) <= 26:
                    ways += helper(idx+2)
            
            memo[state] = ways
            return memo[state]

        return helper(0)
