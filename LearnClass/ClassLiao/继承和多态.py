#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@author: Yan Zhaobo
@software: PyCharm Community Edition
"""

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    #pass
    def run(self):
        print('Dog is running...')

class Cat(Dog):
    #pass
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()
cat = Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())