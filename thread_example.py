'''
@Author: SaminShi
@Date: 2019-10-31 23:21:29
@LastEditors  : SaminShi
@LastEditTime : 2020-01-05 17:15:13
@Description: example
@Email: shizhimin0406@163.com
@Company: xxx
@version: 1.0
'''
# -*- coding: utf-8 -*-
import threading,time


class MyThread(threading.Thread):

    def __init__(self,name=None,func=None,args=()):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None


def foo(a,b,c,t=2):
    time.sleep(t)
    return a*2,b*2,c*2

st = time.time()
li = []
for i in range(4):
    t = MyThread(i,foo,args=(i,i+1,i+2))
    
    li.append(t)
    t.start()

for t in li:
    t.join()  # 一定要join，不然主线程比子线程跑的快，会拿不到结果
    print(t.get_result())

et = time.time()
print(et - st)