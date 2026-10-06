class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        end = 1
        max_len = end - start
        while end < len(s) and start <= end:
            if s[end] in s[start:end]:
                start += 1
            else:
                end += 1
                if end - start > max_len:
                    max_len = end - start
        print(start, end)
        return max_len