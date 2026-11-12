class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        faulty = []

        for idx, trip in enumerate(triplets):
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                faulty.append(idx)

        if len(faulty) >= len(triplets):
            return False
        
        a, b, c = False, False, False
        for idx, trip in enumerate(triplets):
            if idx in faulty:
                continue
            if trip[0] == target[0]:
                a = True
            if trip[1] == target[1]:
                b = True
            if trip[2] == target[2]:
                c = True

        if a and b and c:
            return True
        else:
            return False
