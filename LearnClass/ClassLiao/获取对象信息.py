#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Yan Zhaobo
@software: PyCharm Community Edition
"""

class MyDog(object):
    def __len__(self):
        print(100)
        return 100
    def __dir__(self):
        print('yzb')
        return 'yzb'

dog = MyDog()
len(dog)
dir(dog)