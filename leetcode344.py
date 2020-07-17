'''反转字符串'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)//2
        for i in range(0,n):
            s[i],s[-i-1] = s[-i-1],s[i]

