'''
@Author: SaminShi
@Date: 2019-11-03 10:01:48
@LastEditors: SaminShi
@LastEditTime: 2019-11-03 10:49:59
@Description: example
@Email: shizhimin0406@163.com
@Company: xxx
@version: 1.0
'''
# -*- coding: utf-8 -*-
import difflib
import os

filename1 = os.getcwd() + '\\' + 'test_file1.txt'
filename2 = os.getcwd() + '\\' + 'test_file2.txt'

# print(__file__)
# print(os.getcwd())
html_diff = difflib.HtmlDiff()

with open(filename1,'r') as f1:
    filename1_arr = f1.readlines()

with open(filename2,'r') as f2:
    filename2_arr = f2.readlines()

html_content = html_diff.make_file(filename1_arr,filename2_arr)
print(html_content)

with open('diff.html','w') as hfile:
    hfile.write(html_content)