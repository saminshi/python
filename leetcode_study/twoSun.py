'''
@Author: SaminShi
@Date: 2019-10-27 17:56:50
@LastEditors: SaminShi
@LastEditTime: 2019-10-27 22:46:18
@Description: example
@Email: shizhimin0406@163.com
@Company: xxx
@version: 1.0
'''
# -*- coding: utf-8 -*-

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def twoSun(nums, target):
    result = []
    nums_dict = dict(list(enumerate(nums)))
    for n in nums:
        if target - n in nums:
            result = (sorted([nums.index(n),nums.index(target-n)]) if nums.index(n) != nums.index(target-n) else [])
            print(result)
            break
    return result

print(twoSun([3,3],6))


