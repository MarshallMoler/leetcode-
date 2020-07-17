'''字符串中的第一个唯一字符'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for i in s:
            if i not in map.keys():
                map[i] = 1
            else:
                map[i] = map[i] + 1
        for k,v in map.items():
            if v == 1:
                for i in range(len(s)):
                    if k == s[i]:
                        return i
                break
        return -1
