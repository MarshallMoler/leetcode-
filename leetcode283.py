'''移动零'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n1 = nums.count(0)
        if n1 == 0:
            return nums
        for i in range(n1):
            nums.remove(0)
            nums.append(0)
