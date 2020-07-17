'''寻找两个正序数组的中位数'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)//2
        if len(nums1)%2 == 0:
            medium = (nums1[n]+nums1[n-1])/2
            return medium
        else:
            return nums1[n]
