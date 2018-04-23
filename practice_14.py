#!usr/bin/python
# -*- coding:utf-8 -*-
# practice chapter 1 problem 4, ROC plotting rountine
# Apache License: Version 2.0

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

t = np.linspace(1e-4,2,100)
x = norm.cdf(-1*np.sqrt(2)*(0.25+np.log(t)))
y = 1-norm.cdf(-1*np.sqrt(2)*(0.25-np.log(t)))
plt.plot(x,y,'r',linewidth=3)
plt.title('ROC curve',size='x-large')
plt.xlabel('$P_F$',size='large')
plt.ylabel('$P_D$',rotation='horizontal',size='large')
ax = plt.gca()
ax.xaxis.set_label_coords(1.05,0)
ax.yaxis.set_label_coords(-0.025,1)
plt.grid()
plt.savefig('ROC_curve.eps')
plt.show()

