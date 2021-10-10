# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:13:52 2019

@author: haseena
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#Input data that you want to analyse
data = pd.read_excel('Processed data g-file.xlsx' , sheet_name='P200')

params = {'figure.figsize':(6,5)}

plt.rcParams.update(params)

#Solar Luminosity
l0 = 3.838E26
#declare your column
#temp = data.temp
#rho = data.den
#rad = data.rad/1E10
#lr = data.lr
teff = data.teff
pair = data.paired
phot = data.photod
#plas = data.plas
#brem = np.log10(data.brem)
#recomb = data.recomb
#lxx = data.lxx/1E8
#total = data.total
#eps120 = data.epsnu

#print(eps120,rad)

#plotting configuration

#plt.title('(500$M_\odot$)Neutrino H-R diagram',fontsize=15)
#(x, y, color='cyan', label='HR')
plt.plot(teff,pair, color='red', label='$Q_{pair}$')
plt.plot(teff,phot, color='blue', label='$Q_{photo}$')
#plt.plot(phot,lr)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Energy loss -
#plt.xlabel('TEMP ($10^9 K$)')
# Temp9 - plt.xlabel('TEMP ($10^9 K$)')
# Luminosity -plt.xlabel('L)
#RAD (10^10 m)
plt.xlim(4.9,3.75)
plt.ylim(-105,20)
plt.xlabel('$\log_{10}$Teff(K)',fontsize=10) 
plt.ylabel('$\log_{10}$Q[erg/cm\u00b3 s])',fontsize=10)
#(('$\u03C1$ ($10^6$ g /cm\u00b3)'))  # density
#plt.ylim(6.5845E-03,1.4092E+07) #energy
#plt.xlim(1.4189E+02,3.0026E+06) #temp.rho.rad
#plt.legend(loc='center left', fontsize='10')
plt.legend(fontsize=10)
plt.show()
plt.savefig('p200neutrinohr.jpg')

