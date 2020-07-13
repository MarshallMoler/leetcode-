'''加一'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]+1 < 10:
            digits[-1]=digits[-1]+1
            return digits
        else:
            count = 0
            for j in range(-1,-len(digits)-1,-1):
                if digits[j] + 1 == 10:
                    digits[j] = 0
                    count += 1
                else:
                    digits[j] = digits[j]+1
                    break
            if count == len(digits):
                digits.insert(0,1)
            return digits
