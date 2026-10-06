class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sorts = ''.join(sorted(s))
            if sorts in d:
                d[sorts].append(s)
            else:
                d[sorts] = [s]
        return [group for group in d.values()]