class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ## rows become columns but swapped in order
        n = len(matrix)
        newMatrix = [[None] * n for _ in range(n)] 
        for i, row in enumerate(matrix):
            for j, el in enumerate(row):
                newMatrix[j][n - 1 - i] = el
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = newMatrix[i][j]

