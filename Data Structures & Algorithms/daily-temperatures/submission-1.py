class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > temperatures[stack[-1]]:
                j = stack.pop()
                answers[j] = i - j
            stack.append(i)
        return answers



            