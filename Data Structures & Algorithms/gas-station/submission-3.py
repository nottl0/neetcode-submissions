class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # diff = gas - cost
        # [-1, 0, -1, 3]
        # [-1, -1, 1]
        # [-1, 3, -4, 2]
        total = 0
        start = 0
        if sum(gas)-sum(cost) < 0:
            return -1
        for i in range(len(gas)):
            if total < 0:
                total = 0
                start = i
            total += gas[i] - cost[i]
        return start