class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize != 0:
            return False

        hand.sort()
        hmap = {}

        for elem in hand:
            hmap[elem] = hmap.get(elem, 0) + 1
        
        group = []
        while True:
            nonZero = False
            for key in hmap.keys():
                if hmap[key] > 0:
                    nonZero = True
                    if not group or (group and (group[-1] + 1) == key):
                        group.append(key)
                        hmap[key] -= 1
                    else:
                        return False
                if len(group) == groupSize:
                    group = []
                    break
            if not nonZero:  #### IIIMMMPP
                return True
                    
                    
        

        