dict1={'a':1,'b':2,'c':3}
dict2 =dict1.copy()
dict2['c']=4
print(dict1)
print(dict2)
dict1.clear()
print(dict1)
print(dict2)
a=dict2.keys()
print(a)