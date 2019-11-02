#!/usr/bin/env python
# -*- coding: utf-8 -*-
#/*
# * @Author: SaminShi
# * @Date: 2018-06-24 08:35:28
# * @LastEditors: SaminShi
# * @LastEditTime: 2018-06-24 08:42:16
# * @Description: example
# * @Email: shizhimin0406@163.com
# * @Company: xxx
# * @version: 1.0
# */
class C:
    def __init__(self):
        self._x=None

    def getx(self):
        return self._x
    def setx(self,value):
        self._x=value
    def delx(self):
        del self._x
    
    x=property(getx,setx,delx,"I'm the 'x' property.")

c = C()
print("c.x is %s" % c.x)
c.x = 1
print(c.x)
# del c.x
# print(c.x)




class Parrot():
    def __init__(self):
        self._voltage = 10000
    
    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

p = Parrot()
print(p.voltage)




class CC():
    def __init__(self):
        self._x = None
    
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self,value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

cc = CC()
cc.x=23
print(cc.x)
