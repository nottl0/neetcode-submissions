class Solution:
    def isHappy(self, n: int) -> bool:
        def getNumbers(n):
            numbers = []
            while n > 0:
                rem = n % 10
                n = n // 10
                numbers.append(rem)
            return numbers
        seen = set()
        s = n;
        while True:
            numbers = getNumbers(s)
            s = sum([n*n for n in numbers])
            if s == 1:
                return True
            if s in seen:
                return False
            seen.add(s)
        return False
