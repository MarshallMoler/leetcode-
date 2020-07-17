'''寻找旋转排序数组中的最小值'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left < right:
            if nums[left] < nums[right]:
                right -= 1
            else:
                left += 1
        return nums[left]
