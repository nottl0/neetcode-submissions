class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxval = max(piles)
        def getceil(num: int, div: int) -> int:
            if num%div == 0:
                return num//div
            else:
                return int(num//div) + 1 
        mid = maxval
        low = 1
        high = maxval
        while low <= high:
            mid = (high+low)//2
            print(mid, high, low)
            hours = sum(getceil(pile, mid) for pile in piles)
            print(hours)
            # if hours == h:
            #     return mid
            if hours > h:
                low = mid + 1
            else:
                prev = mid
                high = mid - 1
        return prev
            
                
