# '''
# @Author: SaminShi
# @Date: 2019-10-27 17:56:50
# @LastEditors: SaminShi
# @LastEditTime: 2019-11-03 21:12:00
# @Description: example
# @Email: shizhimin0406@163.com
# @Company: xxx
# @version: 1.0
# '''
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

#此方法执行耗时980ms，内存消耗14.8MB
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


del twoSun
#此方法执行耗时832ms，内存消耗14.7MB
def twoSun(nums,target):
    result = []
    for i in range(len(nums)):
        if target - nums[i] in nums[i+1:len(nums)]:
            result = [i,nums[i+1:len(nums)].index(target-nums[i])+i+1]
            break
    return result

print(twoSun([2,5,5,11],10))
print(twoSun([3,3],6))

del twoSun

def twoSun(nums,target):
    nums_dict = dict(list(enumerate(nums)))  #将数组转换为以数组索引为键，以数组元素为值的哈希表 {0: 2, 1: 7, 2: 11, 3: 15}
    result = []
    while True:
        nums_pop_tumple = nums_dict.popitem()
        if len(result) == 0:
            if target - nums_pop_tumple[1] in nums_dict.values():
                result.append(nums_pop_tumple[0]) 
            
            continue
            
        if nums_pop_tumple[1] == target - nums[result[0]]:
            result.append(nums_pop_tumple[0]) 
            break
        if len(nums_dict) == 0: break
    return(sorted(result))


print(twoSun([2,5,5,11],10))
print(twoSun([3,3],6))

del twoSun

# '''
# 作者：lao-la-rou-yue-jiao-yue-xiang
# 链接：https://leetcode-cn.com/problems/two-sum/solution/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# '''
def twoSum(nums, target):
    hashmap={}
    for i,num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i,hashmap.get(target - num)]
        hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况

