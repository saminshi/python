'''
@Author: SaminShi
@Date: 2019-10-27 17:56:50
@LastEditors: SaminShi
@LastEditTime: 2019-11-03 17:20:55
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
    for n in nums:
        if target - n in nums:
            if nums.index(n) != nums.index(target-n):
                result = sorted([nums.index(n),nums.index(target-n)])
            else:
                nums_dict = dict(list(enumerate(nums)))  #将数组转换为以数组索引为键，以数组元素为值的哈希表 {0: 2, 1: 7, 2: 11, 3: 15}
                nums_dict.pop(nums.index(n))
                for k in nums_dict.keys():
                    result = (sorted([nums.index(n),k]) if nums_dict[k] == target-n else [])
                    if result != []:
                        break
            
            #print(result)
        if result != []:
            break
    return result

print(twoSun([2,5,5,11],10))
print(twoSun([3,3],6))


