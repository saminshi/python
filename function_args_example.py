'''
@Author: SaminShi
@Date: 2019-10-31 23:21:29
LastEditors: Please set LastEditors
LastEditTime: 2021-03-28 11:39:04
@Description: example
@Email: shizhimin0406@163.com
@Company: xxx
@version: 1.0
'''
# -*- coding: utf-8 -*-
a = (1,2,3,{'a':1})


def func(args,name="ka",*ar,**kwargs):
    kwargs.update(c=3)
    print('The args : %s,the name : %s, the ar : %s, the kwargs : %s'%(args,name,ar,kwargs))

dict_x = {'b':2}

func(1,*a,**dict_x)

func(a)


def add_end(l = []):
    l.append('END')
    return l


b=add_end()
print(b)
c=add_end()
print(c)