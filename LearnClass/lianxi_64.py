#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Yan Zhaobo
@software: PyCharm Community Edition
编写⼀个跟踪商品销售的类，这个类的对象将拥有如下属性：
    1.销售数量
    2.每件商品的单价
    3.批发起始数量
    4.批发折扣百分⽐
并且拥有如下⽅法：
    1.register_sale(n)，记录n件商品的销售，
    如果n⼤于批发数量，则按照批发价格销售
    2.display_sale()，显⽰销售数量、销售总额
要求：创建实例，并调⽤display_sale()⽅法，显⽰销售数量个销售总额。
"""

class ShangPin(object):
    def __init__(self, price, num_pi, baifenbi):
        self.num = 0    #销售数量
        self.totle = 0  #销售总额
        self.price = price
        self.num_pi = num_pi
        self.baifenbi = baifenbi
    def register_sale(self, n):
        if(n > self.num_pi):
            self.totle += n * self.price * self.baifenbi
        else:
            self.totle += n * self.price
        self.num += n   #计算总销售量
        self.totle #计算销售总额
    def display_sale(self):
        print(("销售数量：{0}"+'\n'+"销售总额：{1}").format(self.num, self.totle))

kuzi = ShangPin(100, 10, 0.5)
kuzi.register_sale(50)
kuzi.display_sale()
