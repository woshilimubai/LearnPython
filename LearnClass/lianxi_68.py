#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Yan Zhaobo
@software: PyCharm Community Edition
"""

import math

class Dot(object):
    def __init__(self,tuple_position):
        #assert isinstance(position, list), "坐标值的形式必须是元组或者列表"
        #assert (isinstance(position[0], float or int) and isinstance(position[1], float or int)), "坐标值应为数字"
        self.x = tuple_position[0]
        self.y = tuple_position[1]

class Calculate(object):
    def __init__(self, dot_1, dot_2):
        self.x_1 = dot_1.x
        self.y_1 = dot_1.y
        self.x_2 = dot_2.x
        self.y_2 = dot_2.y

    def Distance(self):
        distance = math.sqrt((self.x_1-self.x_2) ** 2 + (self.y_1-self.y_2) ** 2)
        print("两点之间的距离是{:.2f}".format(distance))

    def ShiLiang(self):
        shiliang = ((self.x_2 - self.x_1), (self.y_2 - self.y_1))
        print(shiliang)

if __name__ == "__main__":
    dot1 = Dot((1, 5))
    dot2 = Dot((4, 9))
    a = Calculate(dot1, dot2)
    a.Distance()
    a.ShiLiang()

