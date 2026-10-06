class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x = 0
        y = len(heights) - 1
        maxArea = 0
        while x < y:
            curr = min(heights[x], heights[y]) * (y -x)
            print(x, y)
            print(curr)
            if curr > maxArea:
                print(x, y)
                maxArea = curr
            if heights[x] < heights[y]:
                x += 1
            else:
                y -= 1
             
        return maxArea

            
        