#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Yan Zhaobo
@software: PyCharm Community Edition
"""

class RoundFloat(object):
    def __init__(self, val):
        assert isinstance(val, float),"value must be a float"
        self.val = round(val, 2)

    def __str__(self):
        return "{:.2f}".format(self.val)

    __repr__ = __str__

if __name__ == "__main__":
    while(True):
        n = input("Input a float:('q'-exit)")
        if n == 'q':
            print('See you next time.')
            break
        else:
            n = float(n)
            r = RoundFloat(n)
            print(r)