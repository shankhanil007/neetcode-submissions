class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed))
        fleet = 0
        times = []

        for car in cars:
            time = (target - car[0]) / car[1]
            times.append(time)

        stack = []
        for time in times:
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)

        return len(stack)
        