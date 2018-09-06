#! /usr/bin/env python
# -*-coding:UTF-8-*-
"""
-----------------------------------------------------------
@author : pan
@time:  
"""
import matplotlib.pyplot as plt


class block(object):
    def __init__(self, member, rules):
        self.member = member        # member is a list that contains the streams and the buildings
        self.rules = rules          # rules tell the form which the elements have
        self.time = 0

    def show(self, show=0):
        plt.imshow(self.rules(self.member)) #camp=plt.cm.winter)
        plt.axis('off')
        plt.title('Iter :{}'.format(self.time))
        if show == 0:
            plt.show()
        elif show == 1:
            plt.savefig('png/' + str(self.time) + '.png')

    def update(self):
        for stream in self.member[0]:
            stream.update()
        self.time += 1
