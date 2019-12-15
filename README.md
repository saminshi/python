<!--
 * @Author: SaminShi
 * @Date: 2019-12-14 13:36:42
 * @LastEditors: SaminShi
 * @LastEditTime: 2019-12-15 09:48:06
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
'''
@Author: SaminShi
@Date: 2018-04-22 10:46:55
@LastEditors: SaminShi
@LastEditTime: 2019-12-01 09:13:58
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
