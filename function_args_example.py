'''
@Author: SaminShi
@Date: 2019-10-31 23:21:29
@LastEditors: SaminShi
@LastEditTime: 2019-11-02 09:46:17
@Description: example
@Email: shizhimin0406@163.com
@Company: xxx
@version: 1.0
'''
# -*- coding: utf-8 -*-
a = (1,2,3,{'a':1})


def func(args,name="ka",*ar,**kwargs):
    print('The args : %s,the name : %s, the ar : %s, the kwargs : %s'%(args,name,ar,kwargs))

dict_x = {'b':2}

func(1,*a,**dict_x)
func(a)