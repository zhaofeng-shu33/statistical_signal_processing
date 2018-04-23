#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# plot a three element hypothesis testing (one-dimensional) graph
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# see signal_detection.pdf for detail

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1,figsize=(20,10))
x = np.linspace(-4,5,200)
ax.plot(x,norm.pdf(x,loc=1),'r',linewidth=3)
ax.plot(x,norm.pdf(x,loc=2),'b',linewidth=3)
ax.plot(x,norm.pdf(x,loc=-1),'g',linewidth=3)

ax.plot([0,0],[0,0.42],'k--')
ax.plot([1.5,1.5],[0,0.42],'k--')

plt.xlabel('z',fontsize=36)
plt.ylabel('pdf',fontsize=36)
plt.title('3-element hp testing',fontsize=36)
ax.tick_params(labelsize=24)
plt.savefig('3meta_hpt.eps')
plt.show()

