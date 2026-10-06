class Solution:
    def isValid(self, s: str) -> bool:
        brack_stack = []
        brack_chars = {')': '(', 
                        '}': '{', 
                        ']': '['}
        for c in s:
            if c in brack_chars.keys():
                if len(brack_stack):
                    el = brack_stack.pop()
                    if brack_chars[c] != el:
                        return False
                else:
                    return False
            else:
                brack_stack.append(c)
        return len(brack_stack) == 0
            
