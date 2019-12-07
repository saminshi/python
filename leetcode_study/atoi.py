'''
@Author: SaminShi
@Date: 2019-11-30 18:06:21
@LastEditors: SaminShi
@LastEditTime: 2019-11-30 18:11:39
@Description: example
@Email: shizhimin0406@163.com
@Company: xxx
@version: 1.0
'''
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


str1 = '12345'
int1 = Solution().myAtoi(s=str1)
print(int1)