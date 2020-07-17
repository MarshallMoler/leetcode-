'''有效的字母异位词'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list_s = sorted(list(s))
        list_t = sorted(list(t))
        return list_s == list_t
