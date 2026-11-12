class TimeMap:

    def __init__(self):
        self.hmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append((timestamp, value))
        else:
            self.hmap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        
        res, arr = "", self.hmap.get(key, [])
        l, h = 0, len(arr) - 1
        while l <= h:
            mid = (l+h)//2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                h = mid - 1

        return res


