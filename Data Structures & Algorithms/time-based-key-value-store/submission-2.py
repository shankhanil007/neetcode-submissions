class TimeMap:

    def __init__(self):
        self.hmap = defaultdict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap.keys():
            self.hmap[key].append((timestamp, value))
        else:
            self.hmap[key] = [(timestamp, value)]


    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hmap.keys():
            return ""
        
        values = self.hmap[key]
        l = 0 
        h = len(values)-1
        while l < h:
            mid = (l+h+1)//2                    ### IMP
            if values[mid][0] == timestamp:
                return self.hmap[key][mid][1]
            elif values[mid][0] < timestamp:
                l = mid                         ## IMP
            else:
                h = mid - 1
        if timestamp < values[l][0]:        ## IMP
            return ""
        else:
            return self.hmap[key][l][1]
        
