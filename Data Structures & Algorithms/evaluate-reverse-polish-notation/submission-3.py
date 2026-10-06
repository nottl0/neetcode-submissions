class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        def evalOne(a, b, op):
            if op == "+":
                return a+b
            elif op == "-":
                return a-b
            elif op == "*":
                return a*b
            else:
                return int(a/b)

        self.stack = []
        for c in tokens:
            if c not in ops:
                self.stack.append(c)
            else:
                b = int(self.stack.pop())
                a = int(self.stack.pop())
                ans = evalOne(a, b, c)
                self.stack.append(ans)
        return int(self.stack.pop())
