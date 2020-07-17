'''寻找重复数'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}
        for i in nums:
            if i not in map:
                map[i]=0
            else:
                return i
