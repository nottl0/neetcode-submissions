class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            try:
                d[n] += 1
            except:
                d[n] = 1
        
        sorted_l = sorted(list(d.keys()), key=lambda x: -d[x])[:k]
        return sorted_l