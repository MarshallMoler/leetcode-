'''实现 strStr()'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        h = len(haystack)
        n = len(needle)
        for i in range(h):
            if h-(i+n-1) >= 0:
                if haystack[i:i+n] == needle:
                    return i
                else:
                    continue
        return -1
