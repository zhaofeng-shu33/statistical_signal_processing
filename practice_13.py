#!usr/bin/python
# -*- coding:utf-8 -*-
# practice chapter 1 problem 3, signal detection plotting routine
# Apache License: Version 2.0

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
x = np.logspace(-6,3,100)
x1 = -1*np.sqrt(x)*np.sqrt(0.5-np.sqrt(3)/4)
y = norm.cdf(x1)
plt.plot(10*np.log(x)/np.log(10),y,'r',linewidth=3)
plt.title('$\\bar{R}\\sim \\frac{2E}{N_0}$',size = 'x-large')
plt.xlabel('$\\frac{2E}{N_0}/dB$',size = 'large')
plt.ylabel('$\\bar{R}$',rotation='horizontal',size = 'large')
ax = plt.gca()
ax.xaxis.set_label_coords(1.05,0)
ax.yaxis.set_label_coords(-0.025,1)
plt.grid()
plt.savefig('average_error_with_SNR.eps')
plt.show()

