class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursion 
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        # DP
        if n == 1:
            return 1
        if n == 2:
            return 2
        l = [1] * n
        l[1] = 2
        for i in range(2, n):
            l[i] = l[i-1] + l[i-2]
        return l[-1]
