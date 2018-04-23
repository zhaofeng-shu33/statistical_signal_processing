#!usr/bin/python
# -*- coding:utf-8 -*-
# draw ROC curve and SNR \sim P_D for random phase detection case, signal detection plotting routine
# Apache License: Version 2.0

# implementation of Marcum function : scipy.stats.ncx2
# Q(a,b)=1-ncx2.cdf(b^2,df=2,nc=a^2)

from scipy.stats import ncx2
import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(0.01,0.99,100)
# a^2=r
# r=1
P_D_1 = 1-ncx2.cdf(-2*np.log(alpha),df=2,nc=1)
# r=1.5
P_D_2 = 1-ncx2.cdf(-2*np.log(alpha),df=2,nc=1.5)

plt.plot(alpha,P_D_1,'r',linewidth=3)
plt.plot(alpha,P_D_2,'b',linewidth=3)
plt.xlabel('$\\alpha$')
plt.ylabel('$P_D$',rotation='horizontal')
plt.title('ROC curve')

plt.savefig('ROC_random_phase.eps')
plt.show()

# next fix alpha draw r(dB) \sim P_D

r = np.logspace(0.5,1.9,100)
alpha_1 = 1e-5
P_D_1 = 1-ncx2.cdf(-2*np.log(alpha_1),df=2,nc=r)
alpha_2 = 1e-6
P_D_2 = 1-ncx2.cdf(-2*np.log(alpha_2),df=2,nc=r)

# power ratio
r_db = 10*np.log(r)/np.log(10)
plt.plot(P_D_1,r_db,'r',linewidth=3)
plt.plot(P_D_2,r_db,'b',linewidth=3)
plt.xlabel('$P_D$')
plt.ylabel('$\\frac{2E_s}{N_0}(dB)$',rotation='horizontal')
plt.title('$P_D \\sim$ SNR')

plt.savefig('P_D_sim_SNR.eps')
plt.show()

