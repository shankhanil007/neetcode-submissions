class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed))
        time = []
        for car in cars:
            ctime = (target-car[0])/car[1]
            time.append(ctime)
        stack = []
        for t in time:
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)

        return len(stack)