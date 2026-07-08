class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True) ## IMP see how to sort and ZIP in python
        fleet = []
        for pos, spd in cars:
            time = (target-pos)/spd ## IMP (target-post+1) this +1 is effective for round up only when divided by 2
            if len(fleet) == 0:
                fleet.append(time)
            else:
                if time > fleet[-1]:
                    fleet.append(time)
        return len(fleet)
