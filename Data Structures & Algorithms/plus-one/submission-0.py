class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        transfer = 1
        for i in range(len(digits)-1, -1, -1):
            v = digits[i]
            s = v + transfer
            if s >= 10:
                digits[i] = s - 10
                transfer = s // 10 
            else:
                digits[i] = s
                transfer = 0
        if transfer == 1:
            digits.append(0)
            for i in range(1, len(digits)):
                digits[i] = digits[i-1]
            digits[0] = 1
        return digits 
        