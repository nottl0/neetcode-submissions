import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 
        end = len(s1) - 1
        end_window = len(s2) - end
        d = {}
        e = {}
        for letter in string.ascii_lowercase:
            d[letter] = 0
            e[letter] = 0
        for l in s1:
            d[l] += 1
        for l in s2[:len(s1)]:
            e[l] += 1
        if e == d:
            return True
        for i in range(1, len(s2) - end):
            e[s2[i-1]] -= 1
            e[s2[i+end]] += 1
            if e == d:
                return True
        return False
            
            
