class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oc = {"{":"}", "[":"]", "(":")"}
        for c in s:
            if c in oc:
                stack.append(c)
            else:
                if len(stack) != 0:
                    opener = stack.pop()
                    if oc[opener] != c:
                        return False
                else:
                    return False
        if len(stack) != 0:
            return False
        return True