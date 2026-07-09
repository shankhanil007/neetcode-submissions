class MinStack:

    ## IMP Concept: Store the global min for each element until that index

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        if len(self.arr) == 0:
            self.arr.append((val, val))
        else:
            mval = min(self.getMin(), val)  ## When you POP the global mval will change. So always fetch it first. 
            self.arr.append((val, mval))
        
    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[len(self.arr)-1][0]

    def getMin(self) -> int:
        return self.arr[len(self.arr)-1][1]
        
