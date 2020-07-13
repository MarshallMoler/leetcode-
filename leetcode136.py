'''只出现一次的数字'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        s_data = set(nums)
        for s in s_data:
            count = 0
            for n in nums:
                if s == n:
                    count += 1
            if count == 1:
                break
        return s
