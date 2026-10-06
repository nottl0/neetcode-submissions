class Solution:
    def numDecodings(self, s: str) -> int:
        prev = 1
        prevprev = 1
        curr = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "0":
                curr = prev

            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                curr += prevprev
            prevprev = prev
            prev = curr 
            curr = 0
        return prev