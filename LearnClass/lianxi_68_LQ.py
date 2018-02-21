#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Yan Zhaobo
@software: PyCharm Community Edition
"""

import math

class Point(object):
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({:.2f}, {:.2f})".format(self.x, self.y)

    def distance(self, p):
        dis = math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        return dis

    def sum(self, p):
        x_new = self.x + p.x
        y_new = self.y + p.y
        return Point(x_new, y_new)

if __name__ == "__main__":
    p1 = Point(2.0, 4.0)
    p2 = Point(1.0, 5.0)
    d = p1.distance(p2)
    print("The distance is {0}".format(d))
    s = p1.sum(p2)
    print("The new point is {0}".format(s))