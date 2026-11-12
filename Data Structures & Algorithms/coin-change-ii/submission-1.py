class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)

        memo = {}

        def helper(idx, rem):

            if idx >= n or rem < 0:
                return 0
            if rem == 0:
                return 1

            state = (idx, rem)
            if state in memo:
                return memo[state]

            take = helper(idx, rem-coins[idx]) #### sum not  required
            not_take = helper(idx+1, rem) #### sum not  required
            
            memo[state] = take + not_take
            return memo[state]

        return helper(0, amount)