class TimeMap:

    def __init__(self):
        self.hmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append((timestamp, value))
        else:
            self.hmap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        
        if not key in self.hmap:
            return ""
            
        arr = self.hmap[key]
        l, h = 0, len(arr) - 1
        while l <= h:
            mid = (l+h)//2
            if arr[mid][0] < timestamp:
                l = mid + 1
            elif arr[mid][0] > timestamp:
                h = mid - 1
            else:
                return arr[mid][1]
        mini = min(l, h)
        if arr[mini][0] < timestamp:
            return arr[mini][1]     
        else:
            return ""   
