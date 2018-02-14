#!/usr/bin/env python
class Person:
    """
    This is a sample of class.
    """

    def __init__(self, name):
        self.name = name

    def get_neme(self):
        return self.name

    def color(self, color):
        d = {}
        d[self.name] = color
        return d

