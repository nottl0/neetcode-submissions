class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distance = [target - p for p in position]
        sdistance = sorted(distance)
        sorted_indeces = sorted(range(len(position)), key=lambda i: distance[i])
        times = (d/speed[i] for d,i in zip(sdistance, sorted_indeces))
        prev = float("-inf")
        fleets = 0
        for t in times:
            if t > prev:
                fleets += 1
                prev = t
        return fleets
