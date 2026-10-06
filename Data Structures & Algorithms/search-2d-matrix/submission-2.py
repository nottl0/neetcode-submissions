class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startRow = 0
        for i in range(len(matrix)):
            startRow = i
            if matrix[i][0] > target:
                startRow = i - 1
                break
            if matrix[i][0] == target:
                return True
        start = 0
        end = len(matrix[0]) - 1 
        while start <= end:
            mid = (start+end)//2
            print(mid)
            if target == matrix[startRow][mid]:
                return True
            elif target > matrix[startRow][mid]:
                start = mid + 1
            else:
                end = mid - 1
        return False
