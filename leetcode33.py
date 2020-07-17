'''搜索旋转排序数组'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right = n-1
        while left<= right:
            if nums[left]!=target and nums[right] != target :
                left += 1
                right -= 1
            elif nums[left] == target:
                return left
            else:
                return right
        return -1
