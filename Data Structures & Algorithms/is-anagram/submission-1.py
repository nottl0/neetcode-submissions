from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = Counter(s)
        set_t = Counter(t)
        if set_s == set_t:
            return True
        return False