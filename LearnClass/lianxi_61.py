#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@author: Yan Zhaobo
@software: PyCharm Community Edition
创建类SchoolKid，初始化⼩孩的姓名、年龄。也有访问每个属性的⽅法和修改属性的⽅法。然
后创建类ExaggeratingKid，继承类SchoolKid，⼦类中覆盖访问年龄的⽅法，并将实际年龄加2。
"""

class SchoolKid(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
        return self.age

class ExaggeratingKid(SchoolKid):
    def get_age(self):
        return self.age + 2


if __name__ == '__main__':
    tom = SchoolKid('Tom', 12)
    print(tom.get_name())
    print(tom.get_age())
    print(tom.set_name('Tom'))
    print(tom.set_age(28))

    tom2 = ExaggeratingKid('Tom2', 14)
    print(tom2.get_name())
    print(tom2.get_age())
    tom2.set_age(12)
    print(tom2.get_age())

