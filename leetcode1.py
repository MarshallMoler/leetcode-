'''两数之和'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            find_value = target-nums[i]
            for j in range(n):
                if find_value == nums[j] and i != j:
                    return [i,j]
