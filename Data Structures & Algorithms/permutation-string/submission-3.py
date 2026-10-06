class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import string
        end = len(s1) - 1
        s1_letters = {l:0 for l in string.ascii_lowercase}
        window_letters = {l:0 for l in string.ascii_lowercase}
        for s in s1:
            s1_letters[s] += 1
        # count elements in a window
        for s in s2[:end+1]:
            window_letters[s] += 1
        if window_letters == s1_letters:
            return True
        for i in range(1, len(s2) - end):
            window_letters[s2[i - 1]] -= 1
            window_letters[s2[i + end]] += 1
            if window_letters == s1_letters:
                return True
        return False