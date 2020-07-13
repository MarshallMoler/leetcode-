'''存在重复元素'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        s_data = set(nums)
        if n > len(s_data):
            return True
        else:
            return False
