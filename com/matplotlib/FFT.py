#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/16 22:44
# @Author  : Jasontang
# @Site    : 
# @File    : FFT.py
# @ToDo    : 快速傅里叶变换


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def triangle_wave(size, T):
	t = np.linspace(-1, 1, size, endpoint=False)
	y = np.abs(t)
	y = np.tile(y, T) - 0.5
	x = np.linspace(0, 2*np.pi*T, size*T, endpoint=False)
	return x, y

def sawttooth_wave(size, T):
	t = np.linspace(-1, 1, size)
	y = np.title(t, T)
	x = np.linspace(0, 2*np.pi*T, size*T, endpoint=False)
	return x, y

def triangle_wave2(size, T):
	x, y = sawttooth_wave(size, T)
	return x, np.abs(y)

def none_zero(f):
	f1 = np.real(f)
	f2 = np.imag(f)
	eps = 1e-4
	return f1[(f1 > eps) | (f1 < -eps)], f2[(f2 > eps) | (f2 < -eps)]

if __name__ == '__main__':
	mpl.rcParams['font.sans-serif'] = 'SimHei'
	mpl.rcParams['axes.unicode_minus'] = False
	np.set_printoptions(suppress=True)

	x = np.linspace(0, 2*np.pi, 16, endpoint=False)
	print '时域采样值：', x
	y = np.sin(2*x) + np.sin(3*x + np.pi/4) + np.sin(5*x)

	N = len(x)
	print '采样点个数:', N
	print "\n原始信号:", y

	f = np.fft.fft(y)
	print "\n频域型号:", f/N
	a = np.abs(f/N)
	print '\n频率强度:', a

	iy = np.fft.fft(f)
	print "\n逆傅里叶变换恢复信号：", iy
	print "\n虚部：", np.imag(iy)
	print "\n实部：", np.real(iy)
	print "\n恢复信号与原始信号是否相同:", np.allclose(np.real(iy), y)

	# 分成2行1列，使用第一个子图
	plt.subplot(211)
	plt.plot(x, y, 'go-', lw=2)
	plt.title(u"时域信号", fontsize=15)
	plt.grid(True)

	# 分成2行1列，使用第二个子图
	plt.subplot(212)
	w = np.arange(N) * 2 * np.pi / N
	print "频率采样值:" , w
	plt.stem(w, a, linefmt='r-', markerfmt='ro')
	plt.title(u"频率信号", fontsize=15)
	plt.grid(True)
	plt.show()

	# 三角/锯齿波
	x, y = triangle_wave(20, 5)
	N = len(y)
	f = np.fft.fft(y)
	print '原始频率信号:', none_zero(f)
	a = np.abs(f / N)

	f_real = np.real(f)
	eps = 0.1 * f_real.max()
	print "f_real = \n", f_real
	print eps
	f_real[(f_real < eps) & (f_real > -eps)] = 0
	f_imag = np.imag(f)
	eps = 0.3 * f_imag.max()
	print eps
	f_imag[(f_imag < eps) & (f_imag > -eps)] = 0
	f1 = f_real + f_imag * 1j
	y1 = np.fft.ifft(f1)
	y1 = np.real(y1)
	print "恢复频率信号:", none_zero(f)

	plt.figure(figsize=(8, 18))
	# 分成3行1列，使用第一个子图
	plt.subplot(311)
	plt.plot(x, y, 'g-', lw=2)
	plt.title(u'三角波', fontsize=15)
	plt.grid(True)

	# 分成3行1列，使用第二个子图
	plt.subplot(312)
	w = np.arange(N) * 2 * np.pi / N
	plt.stem(w, a, linefmt='r-', markerfmt='ro')
	plt.title(u'频率信号', fontsize=15)
	plt.grid(True)

	# 分成3行1列，使用第三个子图
	plt.subplot(313)
	plt.plot(x, y1, 'b-', lw=2, markersize=4)
	plt.title(u'三角波恢复信号', fontsize=15)
	plt.tight_layout(1.5, rect=[0, 0.04, 1, 0.96])
	plt.suptitle(u'快速傅里叶变换FFT与频域滤波', fontsize=18)
	plt.show()


