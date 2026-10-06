class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curr = ""
        num_to_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def dfs(i):
            nonlocal curr
            if i >= len(digits):
                res.append(curr)
                return 
            for l in num_to_letter[digits[i]]:
                curr += l
                dfs(i+1)
                curr = curr[:-1]
        if len(digits) == 0:
            return res
        dfs(0)
        return res
            
            
