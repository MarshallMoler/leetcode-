'''x 的平方根'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<= 1:
            return x
        left = 0
        right = x
        ans = -1
        while left<= right:
            mid = (left+right)//2
            if mid*mid > x:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        return int(ans)
