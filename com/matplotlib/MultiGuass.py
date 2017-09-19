#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/16 12:21
# @Author  : Jasontang
# @Site    : 
# @File    : MultiGuass.py
# @ToDo    : 多元高斯分布

import numpy as np
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = 'SimHei'

if __name__ == '__main__':
	x1, x2 = np.mgrid[-5:5:51j, -5:5:51j]

	x = np.stack((x1, x2), axis=2)
	plt.figure(figsize=(9, 8))
	sigma = (np.identity(2), np.diag((3,3)), np.diag((2, 5)), np.array(((2,1), (2,5))))

	for i in np.arange(4):
		ax = plt.subplot(2, 2, i+1, projection='3d')
		norm = stats.multivariate_normal((0, 0), sigma[i])
		y = norm.pdf(x)
		ax.plot_surface(x1, x2, y, cmap=cm.ocean, rstride=2, cstride=2, alpha=0.9, lw=0.3)
		ax.set_xlabel("X")
		ax.set_ylabel("Y")
		ax.set_zlabel("Z")
	plt.suptitle(u"二元高斯分布方差比较", fontsize=18)
	plt.tight_layout(1.5)
	plt.show()