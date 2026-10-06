class MinStack:

    def __init__(self):
        self.stack = list()
        self.minind = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minind) != 0:
            if self.stack[self.minind[-1]] > val:
                self.minind.append(len(self.stack)-1)
            else:
                self.minind.append(self.minind[-1])
        else:
            self.minind.append(len(self.stack)-1)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.minind = self.minind[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minind[-1]]
