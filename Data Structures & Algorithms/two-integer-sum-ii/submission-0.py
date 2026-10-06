class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = 0
        y = len(numbers) - 1
        while x != y:
            sumNum = numbers[x] + numbers[y]
            if sumNum  == target:
                return [x+1, y+1]
            elif sumNum > target:
                y -= 1
            else:
                x += 1
        return [None, None]