'''寻找峰值'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        elif len(nums) ==2:
            ret = 1 if nums[0] < nums[1] else 0
            return ret
        left = 0
        right = left + 2
        while right <= len(nums)-1:
            mid = left + 1
            if left==0 and nums[left]>nums[mid]:
                return 0
            elif nums[mid]>nums[left] and nums[mid]>nums[right]:
                return mid
            elif right==len(nums)-1 and nums[right]>nums[right-1]:
                return right
            else:
                left += 1
                right = left + 2

