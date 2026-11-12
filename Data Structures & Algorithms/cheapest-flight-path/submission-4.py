class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0                    ### IMMMMPP

        for itr in range(1, k+2): 
            temp = prices[:]
            for s, d, cost in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + cost < temp[d]:
                    temp[d] = prices[s] + cost
            prices = temp[:]

        return -1 if prices[dst] == float("inf") else prices[dst]
