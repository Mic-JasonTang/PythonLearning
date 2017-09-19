#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/3 19:26
# @Author  : Jasontang
# @Site    : 
# @File    : sqrt.py
# @ToDo    : 给一个数开方，精确值为e^-6


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math


def func(a):
    if a < 1e-6:
        return 0
    last = a
    c = a / 2
    while math.fabs(c - last) > 1e-6:
        last = c
        c = (c + a/c) / 2
    return c

if __name__ == '__main__':
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    x = np.linspace(0, 30, num=50)
    # y2 = [0] * 50
    # i = 0
    # for num in x:
    #     y2[i] = (num ** 0.5)
    #     i += 1
    # print y2
    func_ = np.frompyfunc(func, 1, 1)
    y = func_(x)
    # print "len(x)=", len(x), "len(y)=", len(y), "len(y2)=", len(y2)
    plt.figure(figsize=(10, 5), facecolor='w')
    plt.plot(x, y, 'yo-', lw=2, markersize=6)
    # plt.plot(x, y2, 'g+-', lw=2, markersize=6)
    plt.grid(b=True, ls=":")
    plt.xlabel(u'X', fontsize=16)
    plt.ylabel(u'Y', fontsize=16)
    plt.title('SQRT', fontsize=18)
    plt.show()