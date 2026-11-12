class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = sorted(zip(position, speed))
        stack = []

        for fleet in fleets:
            time = (target-fleet[0])/fleet[1]
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)

        return len(stack)