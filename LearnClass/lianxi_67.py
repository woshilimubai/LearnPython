#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Yan Zhaobo
@software: PyCharm Community Edition
请编写一个迭代器，通过循环语句，实现证书的依次递减1，直到0
"""

class ReverseRange:
    def __init__(self, n):
        self.n = n

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        return self.n

    def __iter__(self):
        return self
for i in ReverseRange(9):
    print(i)