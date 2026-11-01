import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars: list[tuple[int, int]] = [] # tuple[position, speed]
        for p, s in zip(position, speed):
            cars.append((p, s))
        cars.sort()

        topTime: float = 0
        fleets: int = 0
        while cars:
            p, s = cars.pop()
            time = (target - p) / s
            if time > topTime:
                topTime = time
                fleets += 1
        
        return fleets
