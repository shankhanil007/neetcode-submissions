class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start = 0
        capacity = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            capacity = capacity + (gas[i] - cost[i])
            if capacity < 0:
                start = i + 1
                capacity = 0

        return start


