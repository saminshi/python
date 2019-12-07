'''
@Author: SaminShi
@Date: 2019-10-27 16:24:43
@LastEditors: SaminShi
@LastEditTime: 2019-12-01 09:35:47
@Description: example
@Email: shizhimin0406@163.com
@Company: xxx
@version: 1.0
'''
# -*- coding:utf-8 -*-

#学习网址：https://www.runoob.com/w3cnote/python-func-decorators.html
# ---------------第一步：一切皆对象，将函数赋值给一个变量
def hi(name="yasoob"):
    return "hi " + name

print(hi())       #output: 'hi yasoob'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个

print(greet())  # output: 'hi yasoob'

# 如果我们删掉旧的hi函数，看看会发生什么！
del hi
# print(hi())
#outputs: NameError

#如果删除hi 对greet无影响
print(greet())   #outputs: 'hi yasoob'


# ---------------第二步：在函数中定义函数
def hi(name ="yas0ob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back int the hi() function")

hi()
#output:now you are inside the hi() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the hi() function
# 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如：
#greet()
#outputs: NameError: name 'greet' is not defined

del hi


# ---------------第三步：从函数中返回函数
def hi(name='yasoob'):
    def greet():
        return "now you are in the greet() function"
    
    def welcome():
        return "now you are in the welcome() function"
    
    if name == "yasoob":
        return greet
    else:
        return welcome

a = hi()
print(a)  #outputs: <function greet at 0x7f2143c01500>
#上面清晰地展示了`a`现在指向到hi()函数中的greet()函数

print(a())   #outputs: now you are in the greet() function
del hi


# ---------------第四步：将函数作为参数传给另一个函数
def hi():
    return "hi yasoob!"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi)
#outputs:I am doing some boring work before executing hi()
#        hi yasoob!
del hi


