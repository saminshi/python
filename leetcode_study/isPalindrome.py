'''
@Author: SaminShi
@Date: 2020-02-05 10:26:55
@LastEditors  : SaminShi
@LastEditTime : 2020-02-05 15:33:59
@Description: example
@Email: shizhimin0406@163.com
@Company: xxx
@version: 1.0
'''
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数


class Solution:
    @classmethod
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        elif 0 <= x < 10:
            return True
        else:
            reversed_x = 0
            while x > reversed_x:
                reversed_x = reversed_x * 10 + x % 10
                x = int(x/10)
                print(reversed_x)
            return x == reversed_x or x == int(reversed_x/10)


a = 121


# b = Solution()

print(Solution.isPalindrome(a))
