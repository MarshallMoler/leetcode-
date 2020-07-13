'''验证回文字符串'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        return s == s[::-1]
        # if len(s) < 1:
        #     return True
        # s = s.lower()
        # res = ""
        # for i in s:
        #     if i.isalpha() or i.isdigit():
        #         res += i
        # n = len(res)
        # if n <= 1:
        #     return True
        # center_index = n//2
        # left_pointer = 0
        # right_pointer = -1
        # while left_pointer<center_index:
        #     if res[left_pointer]==res[right_pointer]:
        #         left_pointer += 1
        #         right_pointer -= 1
        #     else:
        #         return False
        # return True

