#! /usr/bin/env python
# -*-coding:UTF-8-*-
"""
-----------------------------------------------------------
@author : pan
@time:  2018/9/2
"""
import numpy as np
from traffic_stream import stream
from traffic_block import block
import gif
import os


def clean_png():
    for i in os.listdir('png/'):
        os.remove('png/'+str(i))


def join(mem, style=0):
    s = mem[0]
    for i in range(len(mem)):
        if i == 0:
            pass
        else:
            if style == 0:
                s = np.vstack((s, mem[i]))
            elif style == 1:
                s = np.hstack((s, mem[i]))
    return s


if __name__ == '__main__':
    clean_png()

    def f(t):
        if t % 20 in range(10):
            return False
        else:
            return True

    def g(t):
        if t % 20 not in range(10):
            return False
        else:
            return True


    a = stream(0.2, 20, [f, [10]])
    b = stream(0.2, 20, [g, [7]])
    c = stream(0.2, 20, [f, [7]])
    d = stream(0.2, 20, [g, [10]])
    m = np.ones((1,20)) *2
    m[0][10],m[0][11],m[0][12] = 0,0,0
    member = [[a, b, c, d], m]
    def rules(m):
        base = join([join([np.ones((7,10))*3, np.zeros((7,3)), np.ones((7,7))*3], 1),
                     np.zeros((3,20)),
                     join([np.ones((10,10))*3, np.zeros((10,3)), np.ones((10,7))*3], 1)
                     ])
        x1 = join([np.zeros((7,20)), m[0][2].base[:, ::-1], m[1], m[0][0].base, np.zeros((10,20))])
        x2 = np.rot90(join([np.zeros((10,20)), m[0][3].base, m[1], m[0][1].base[:, ::-1], np.zeros((7,20))]))
        return base + x1 + x2


    bl = block(member, rules)

    for i in range(100):
        bl.update()
        bl.show(1)
    gif.get_gif()