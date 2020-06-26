#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

from abc import  ABCMeta, abstractmethod

class A(metaclass=ABCMeta):
    def __init__(self, a):
        self.a = a
    def square_a(self):
        return self.a * self.a

    @abstractmethod
    def tentimes(self):
        pass

class B(A):

    def cube_b(self):
        return self.a * self.a * self.a

    def tentimes(self):
        return self.a * 10

class C(A):

    def as_it_is(self):
        return self.a

    def tentimes(self):
        return self.a * 10



b_obj = C(4)




