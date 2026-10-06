class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        difference = 0
        while len(stones) > 1:
            stones.sort()
            print(stones)
            x = stones.pop()
            y = stones.pop()
            if x != y:
                difference = abs(x-y)
                stones.append(abs(x-y))
            else:
                difference = 0
        if len(stones) == 1:
            difference = stones.pop()
        return difference


