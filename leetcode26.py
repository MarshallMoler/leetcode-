'''删除排序数组中的重复项'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            count = 0
            for j in range(len(nums)):
                if i == nums[j]:
                    count += 1
            if count > 1:
                for j in range(count-1):
                    nums.remove(i)
