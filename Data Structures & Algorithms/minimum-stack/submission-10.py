class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        curr_min = val
        if self.arr:
            curr_min = self.getMin()
        curr_min = min(curr_min, val)
        self.arr.append((val, curr_min))
        
    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]
        
    def getMin(self) -> int:
        return self.arr[-1][1]
