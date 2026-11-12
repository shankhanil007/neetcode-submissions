class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        fleet = []
        for pos, spd in cars:
            time = (target-pos)/spd
            if len(fleet) == 0:
                fleet.append(time)
            else:
                if time > fleet[-1]:
                    fleet.append(time)
        return len(fleet)
