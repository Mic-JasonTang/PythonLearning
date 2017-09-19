#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/16 20:30
# @Author  : Jasontang
# @Site    : 
# @File    : gamma.py
# @ToDo    : 模拟Gamma函数

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy.special import factorial

mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = "SimHei"

if __name__ == '__main__':
	N = 5
	x = np.linspace(0, N, 50)
	y = gamma(x+1)
	print y
	plt.plot(x, y, "r-", x, y, 'mo', lw=2, ms=7)
	z = np.arange(0, N + 1)
	f = factorial(z, exact=True)
	print f
	plt.plot(z, f, 'go', markersize=9)
	plt.grid(b=True)
	plt.xlim(-0.1, N+0.1)
	plt.ylim(0.5, np.max(y)*1.05)
	plt.xlabel("x", fontsize=15)
	plt.ylabel(u"Gamma(X) - 阶乘" , fontsize=15)
	plt.title(u"阶乘和Gamma函数", fontsize=16)
	plt.show()