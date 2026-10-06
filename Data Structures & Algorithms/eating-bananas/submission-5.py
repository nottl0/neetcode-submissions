class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total_bananas = sum(piles)
        largest_pile = max(piles)
        start_k, end_k = 1, largest_pile
        best_hours = len(piles)
        best_k = largest_pile
        i = 0 
        while start_k <= end_k:
            i += 1
            mid_k = (start_k + end_k) // 2
            mid_hours = sum(map(lambda x: x // mid_k + (x % mid_k >= 1), piles))
            # print(mid_k, best_k)
            # if i >= 5:
            #     break
            if mid_hours > h:
                start_k = mid_k + 1
            else:
                if mid_k <= best_k:
                    end_k = mid_k - 1
                    best_k = mid_k
        return best_k

