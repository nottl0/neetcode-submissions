from collections import defaultdict, Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)
        for s in strs:
            desc = "".join(sorted(s))
            grams[desc].append(s)
        l = [l for l in grams.values()]
        return l