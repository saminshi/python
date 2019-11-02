'''
@Author: SaminShi
@Date: 2019-10-27 18:18:40
@LastEditors: SaminShi
@LastEditTime: 2019-10-27 20:31:57
@Description: example
@Email: shizhimin0406@163.com
@Company: xxx
@version: 1.0
'''
# -*- coding: utf-8 -*-
def add(x:int, y: int) -> int:
    '''
    :param x: int
    :param y: int
    :return: int
    '''
    return x + y

print(help(add))
print(add('hello','world')) ###思考一下这里会报错吗？
print(add.__annotations__)  #{'y': <class 'int'>, 'x': <class 'int'>, 'return': <class 'int'>}
del add
# '''
# Python 3.5引入

# 对函数的参数进行类型注解；

# 对函数的返回值进行类型注解；

# 只对函数参数做一个辅助的说明，并不对函数参数进行类型检查；

# 提供给第三方工具，做代码分析，发现隐藏的bug；

# 函数注解的信息，保存在__annotations__属性中

# 	add.__annotations__

# 	{'y': <class 'int'>, 'x': <class 'int'>, 'return': <class 'int'>}

# 业务应用

#   函数参数类型检查

#   思路：

#     函数参数的检查，一定是在函数外；

#     函数应该作为参数，传入到检查函数中；

#     检查函数拿到函数传入的实际参数，与形参声明对比；

#     __annotations__属性是一个字典，其中包括返回值类型的声明。假设要做位置参数的判断，无法和

#     字典中的声明对应。

#     使用inspect模块

# inspect模块：

#   提供获取对象信息的函数，可以检查函数和类、类型检查。

#   signature(callable)，获取签名(函数签名包括了一个函数的信息，包括函数名，参数类型，它所在的类和名称空间及其他信息)
# '''

import inspect

def add(x:int, y:int,*args, **kwargs) -> int:
    return x + y

sig = inspect.signature(add)
print(sig)

print("param:",sig.parameters)
print("return:",sig.return_annotation)
print(sig.parameters['y'])
print(sig.parameters['x'].annotation)
print(sig.parameters['args'])
print(sig.parameters['args'].annotation)
print(sig.parameters['kwargs'])
print(sig.parameters['kwargs'].annotation)

# '''
# inspect.isfunction(add), 是否是函数；

# inspect.ismethod(add), 是否是类的方法

# inspect.isgenerator(add),  是否是生成器对象；

# inspect.isgeneratorfunction(add), 是否是生成器函数；

# inspect.isclass(add),  是否是类；

# inspect.ismodule(inspect), 是否是模块

# isclass.isbuiltin(print),  是否是内建对象

# 还有很多is函数，需要的时候查阅inspect模块帮助；

# parameter对象

# 	保存在元组中，是只读的；

# 	name, 参数的名字；

# 	annotation, 参数的注解，可能没有定义；

# 	default， 参数的缺省值，可能没有定义；

# 	empty,特殊的类，用来标记default属性或者注释annotation属性的空值；

# 	kind,实参如何绑定到形参，就是形参的类型

# 		POSITIONAL_ONLY ,值必须是位置参数提供

# 		POSITIONAL_OR_KEYWORD, 值可以作为关键字或者位置参数提供；

# 		VAR_POSITIONAL, 可变位置参数，对应*args; 

# 		KEYWORD_ONLY, keyword_only参数，对应*或者*args之后出现的非可变关键字参数；

# 		VAR_KEYWORD, 可变关键字参数，对应**kwargs
#  '''