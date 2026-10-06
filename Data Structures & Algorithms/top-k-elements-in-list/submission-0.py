class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        topk = sorted(d.values(), reverse=True)[:k]
        ans =[]
        for k in d:
            if d[k] in topk:
                ans.append(k)
        return ans
