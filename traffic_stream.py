#! /usr/bin/env python
# -*-coding:UTF-8-*-
"""
-----------------------------------------------------------
@author : pan
@time:  2018/9/5
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as color
import random


class stream(object):
    def __init__(self, rate, length, light=None):
        self.light = light             # light is a function which return the situtation by giving the time
        self.rate = rate               # rate is represent for the speed which the stream goes
        self.length = length
        self.base = np.zeros((1, length))
        self.time = 1

    def show(self, show=0):
        plt.imshow(self.base, cmap=plt.cm.winter)
        plt.axis('off')
        plt.title('Iter :{}'.format(self.time))
        if show == 0:
            plt.show()
        elif show == 1:
            plt.savefig('png/' + str(self.time) + '.png')
    def update(self):
        for i in range(self.length-1,-1,-1):
            if i+1 == self.length:
                self.base[0][i] = 0
            elif self.base[0][i] == 1:
                if self.light is not None and not self.light[0](self.time) and i+1 in self.light[1]:
                    pass
                elif self.base[0][i+1] == 1:
                    pass
                elif self.base[0][i+1] == 0:
                    self.base[0][i+1] = 1
                    self.base[0][i] = 0
        if isinstance(self.rate, int) or isinstance(self.rate, float):
            if random.random() < self.rate:
                self.base[0][0] = 1
            else:
                self.base[0][0] = 0
        elif isinstance(self.rate, function):
            v = self.rate(self.time)
            if random.random() < v:
                self.base[0][0] = 1
            else:
                self.base[0][0] = 0
        self.time += 1







