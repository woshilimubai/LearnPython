#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Yan Zhaobo
@software: PyCharm Community Edition
创建类PayCalculator，拥有属性pay_rate，以每⼩时⼈⺠币数量为单位。拥有⽅法
compute_pay(hours)，计算给给定⼯作时间的报酬，并返回。
"""

class PayCalculator(object):
    def __init__(self, pay_rate, hour):
        self.pay_rate = pay_rate
        self.hour = hour
    def compute_pay(self):
        return self.pay_rate * self.hour

if __name__ == '__main__':
    pay = PayCalculator(10,8)
    print(pay.compute_pay())