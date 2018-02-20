#!/usr/bin/env python3
# coding:utf-8
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if(gender == "male" or gender == "female"):
            self.__gender = gender
        else:
           # print("Error:sex")
           raise ValueError('bad gender')
    def ger_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
if __name__ == "__main__":
    bart = Student('Bart', 'male')
    if bart.get_gender() != 'male':
            print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!')
