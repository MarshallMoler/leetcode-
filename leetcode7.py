'''整数反转'''
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            if str(x)[-1] != "0":
                reverse = int(str(x)[::-1])
            else:
                reverse = int(str(x)[::-1][1:])
        else:
            if str(x)[-1] != "0":
                reverse = str(x)[0]+str(x)[-1:0:-1]
                reverse = int(reverse)
            else:
                reverse = str(x)[0]+str(x)[-1:0:-1][1:]
                reverse = int(reverse
        if reverse > 2**31 -1 or reverse < -2**31:
            return 0
        else:
            return reverse

