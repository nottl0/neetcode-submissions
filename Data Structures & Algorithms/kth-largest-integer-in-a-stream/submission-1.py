class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sorted_h = sorted(nums, reverse=True)[:k]
        self.k = k
    def add(self, val: int) -> int:
        outed_vals = []
        
        while len(self.sorted_h) > 0:
            last = self.sorted_h[-1]
            if val >= last:
                last = self.sorted_h.pop()
                outed_vals.append(last)
                continue
            else:
                break
        if len(self.sorted_h) < self.k:
            self.sorted_h.append(val)
        while len(outed_vals) > 0 and len(self.sorted_h) < self.k:
            outed = outed_vals.pop()
            self.sorted_h.append(outed)
        
        return self.sorted_h[-1]

        
