'''两个数组的交集'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        map = {}
        if n1 < n2:
            for i in nums2:
                if i in nums1:
                    if i in map:
                        map[i]=map[i]+1
                    else:
                        map[i]= 0
        else:
            for i in nums1:
                if i in nums2:
                    if i in map:
                        map[i]=map[i]+1
                    else:
                        map[i]= 0
        return [k for k in map.keys()]
