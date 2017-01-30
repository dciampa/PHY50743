# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:40:26 2017

@author: Drew
"""

import matplotlib.pyplot as plt
import numpy as np

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

def planck(wav, T):
    a = 2.0*h*c**2
    b = h*c/(wav*k*T)
    intensity = a/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity
    
def ray(wav, T):
    a = 2*c*k*T
    intensity = (a)/(wav**4)
    return intensity

# generate x-axis in increments from 1nm to 3 micrometer in 1 nm increments
# starting at 1 nm to avoid wav = 0, which would result in division by zero.
wavelengths = np.arange(1e-9, 3e-6, 1e-9) 

# intensity at 4000K, 5000K, 6000K, 7000K
intensity3000 = planck(wavelengths, 3000.)
intensity5000 = planck(wavelengths, 5000.)
intensity6000 = planck(wavelengths, 6000.)
intensity9000 = planck(wavelengths, 9000.)

ray4000=ray(wavelengths,7000.)


plt.hold(True) # doesn't erase plots on subsequent calls of plt.plot()
plt.plot(wavelengths*1e9, intensity3000, 'r-') 
#plt.plot(wavelengths*1e9, ray4000,'g-')

# plot intensity4000 versus wavelength in nm as a red line
#plt.plot(wavelengths*1e9, intensity5000, 'g-') # 5000K green line
plt.plot(wavelengths*1e9, intensity6000, 'b-') # 6000K blue line
plt.plot(wavelengths*1e9, intensity9000, 'k-') # 7000K black line

#show the plot
plt.show()