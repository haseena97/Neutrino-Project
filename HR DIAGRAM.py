# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:13:52 2019

@author: haseena
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#Input data that you want to analyse
data = pd.read_excel('Processed data g-file.xlsx' , sheet_name='P120')


#Solar Luminosity
l0 = 3.838E26
#declare your column
#temp = data.temp
#rho = data.den
#rad = data.rad/1E10
lr = data.lr
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
plt.style.use('seaborn')
plt.title('(120$M_\odot$)Neutrino H-R diagram')
plt.plot(pair,lr)
plt.plot(phot,lr)
#plt.legend(['plasma_neutrino,bremsstrahlung'])

# Energy loss -
#plt.xlabel('TEMP ($10^9 K$)')
# Temp9 - plt.xlabel('TEMP ($10^9 K$)')
# Luminosity -plt.xlabel('L)
#RAD (10^10 m)
plt.savefig('p120neutrinohr.pdf')
plt.xlabel('$\log_{10}$(Q[erg/scm\u00b3])') 
plt.ylabel('$\log_{10}$(L/$L_\odot$)')
#(('$\u03C1$ ($10^6$ g /cm\u00b3)'))  # density
#plt.ylim(6.5845E-03,1.4092E+07) #energy
#plt.xlim(1.4189E+02,3.0026E+06) #temp.rho.rad
plt.show()


