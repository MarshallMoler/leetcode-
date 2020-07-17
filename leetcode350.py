'''两个数组的交集 II'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        n1 = len(nums1)
        n2 = len(nums2)
        l = []
        if n1 < n2:
            for i in nums1:
                map[i] = nums1.count(i)
            for j in nums2:
                if j in map.keys() and map[j] > 0:
                    l.append(j)
                    map[j] = map[j]-1
        else:
            for j in nums2:
                map[j] = nums2.count(j)
            for i in nums1:
                if i in map.keys() and map[i] > 0:
                    l.append(i)
                    map[i] = map[i]-1
                    
        return l
