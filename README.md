<!--
 * @Author: SaminShi
 * @Date: 2019-12-14 13:36:42
 * @LastEditors: SaminShi
 * @LastEditTime: 2019-12-15 11:57:11
 * @Description: example
 * @Email: shizhimin0406@163.com
 * @Company: xxx
 * @version: 1.0
 -->
# python
# test for python
# test123123123
#----------------------
# aaaaaaaaaaaaaaaaaaaaaaaa
# This is for python test project
# Test Git conflict
#dadfdfa
# this is test for git conflict
def config
def config11
def config22
def config33
def aaaaaa
def aadf
def aadfds
class aaaaaaaaaaaaaa
'''
@Author: SaminShi
@Date: 2019-11-07 20:54:56
@LastEditors: SaminShi
@LastEditTime: 2019-12-08 19:29:06
@Description: example
@Email: shizhimin0406@163.com
@Company: xxx
@version: 1.0
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date    : 2018-04-22 10:15:44
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
class Secretive:

	def __inaccessible(self):   #双下划线开头但不以双下划线结尾的属性或者方法为私有属性或者私有方法，不能从外部直接访问
		print("Bet you can't see me...")

	def accessible(self):
		print("The secret message is:")
		self.__inaccessible()     #可以在内部访问

	def smeth(self):
		print("This is a static method")
	smeth = staticmethod(smeth)

	def cmeth(self,cls):
		print("This is a class method of",cls)
	cmeth = classmethod(cmeth)


class Person:
	grade = 1
	def __init__(self,name):
		self.name = name

	def sayHi(self):#加self区别于普通函数
		print('Hello, your name is?',self.name)

	@staticmethod
	def sayName():#使用了静态方法，则不能再使用self
		print("my name is king") 
		  
	@staticmethod
	def sayAgain():
		print("Again")


	@classmethod
	def classMethod(cls):
		print("class method")

s = Secretive()
s.accessible()
s._Secretive__inaccessible()     #所有以双下划线开始的名字都被“翻译”成前面加上单下划线和类名的形式
print(s.__class__)
Secretive.smeth()
Secretive.cmeth()


p = Person("king")
p.sayHi()
p.sayName()
p.classMethod()
p.sayAgain()
Person.classMethod()
# -*- coding: utf-8 -*-

def command_dict_gereate(frame = 0,slot = 1,pid = 0,ontid = 0,*args,**kwargs):
    bid,portid = slot,pid
    command_dicts = {}
    result_dicts = {}
    line_profile_id = kwargs.get('line_profile_id') or 1
    srv_profile_id = kwargs.get('srv_profile_id') or 1
    command_dicts[0]= [
        'interface gpon 0/{0}'.format(bid),
        'display ont ver {0} {1}'.format(portid,ontid)
        ]

    command_dicts[1]= [
        'interface gpon111 0/{0}'.format(bid),
        'display ont ver1111 {0} {1}'.format(portid,ontid)
        ]
    
    command_dicts[2]= [
        'interface gpon2222 0/{0}'.format(bid),
        'display ont ver2222 {0} {1}'.format(portid,ontid)
        ]
    command_dicts[3]= [
        'interface gpon2222 0/{0}'.format(bid),
        'lineprofile profile {0}'.format(line_profile_id),
        'srvprofile profile {0}'.format(srv_profile_id)
        ]

    if len(args) == 0:
        return None
    else:
        for val in args:
           result_dicts[val] = command_dicts[val]
        return result_dicts

command_list = [1,2]

other_para = {'line_profile_id':2}

print(command_dict_gereate(0,1,2,3,*command_list,**other_para))
