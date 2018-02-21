#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Yan Zhaobo
@software: PyCharm Community Edition
创建⼀个类，输⼊起⽌年⽉⽇，在创建实例之后，通过实例⽅法可以得到的两个⽇期之间的天
数、⽉数和年数（后两者计算整数）
以每月有30天计算
"""

class YearMonthDay(object):
    def __init__(self, listymd):
        self.year = listymd[0]
        self.month = listymd[1]
        self.day = listymd[2]
class DiffYearMonthDay(object):
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def DiffYear(self):
        diff_year = self.end.year - self.start.year
        return diff_year
    def DiffMonth(self):
        diff_year = self.end.year - self.start.year
        diff_month = self.end.month - self.start.month + diff_year * 12
        return diff_month
    def DiffDay(self):
        diff_year = self.end.year - self.start.year
        diff_month = self.end.month - self.start.month + diff_year * 12
        diff_day = diff_month * 30 + self.end.day - self.start.day
        return diff_day
if __name__ == '__main__':
    start = YearMonthDay([2018,2,20])
    end = YearMonthDay([2019,2,21])
    diff = DiffYearMonthDay(start, end)
    #print(diff.start[0])
    print(diff.DiffYear())
    print(diff.DiffMonth())
    print(diff.DiffDay())