class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        t = 0
        r = len(matrix[0])
        b = len(matrix)

        m = b
        n = r
        i, j = 0, 0 
        res = []
        s = 0
        while s < m * n:
            if i == t and j < r:
                res.append(matrix[i][j])
                j += 1
                if j == r:
                    i += 1

            elif j == r and i < b:
                res.append(matrix[i][j - 1])
                i += 1
                if i == b:
                    j -= 1

            elif i == b and j > 0:
                res.append(matrix[i - 1][j - 1])
                j -= 1
                if j == l:
                    i -= 1
            
            else:
                res.append(matrix[i - 1][j])
                i -= 1
                if i == t + 1:
                    t += 1
                    r -= 1
                    l += 1
                    b -= 1
                    i = t
                    j = l
            s += 1
        return res
