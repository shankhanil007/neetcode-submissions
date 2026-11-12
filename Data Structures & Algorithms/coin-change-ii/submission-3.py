class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        memo = {}

        def helper(idx, amt):
            if idx >=n and amt != 0:
                return 0
            
            if amt == 0:
                return 1

            state = (idx, amt)
            if state in memo:
                return memo[state]

            take = 0
            if amt >= coins[idx]:
                take = helper(idx, amt - coins[idx])
            not_take = helper(idx+1, amt)

            memo[state] = take + not_take
            return memo[state]

        return helper(0, amount)