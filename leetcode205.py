'''同构字符串'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        count = 0
        if len(s) <= 1:
            return True
        for i in range(len(s)):
            map1[s[i]] = i
        for j in range(len(t)):
            map2[t[j]] = j
        if len(map1) != len(map2):
            return False
        for n, m in zip(map1.values(), map2.values()):
            if m != n:
                count += 1
        if count == 0:
            return True
        else:
            return False
