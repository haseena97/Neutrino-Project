# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 08:32:24 2019

@author: haseena
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#Input data that you want to analyse
data = pd.read_excel('Processed data g-file.xlsx' , sheet_name='P500')
params = {'figure.figsize':(6,5)}

plt.rcParams.update(params)

#Solar Luminosity
l0 = 3.838E26
#declare your column
#temp = data.temp
#rho = data.den
#rad = data.rad/1E10
#mass = data.mass
age = data.agef
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
#plt.style.use('seaborn')
#plt.title('120$M_\odot$ Kippenhahn diagram',fontsize=15)
plt.plot(age,pair, 'k--', label='$Q_{pair}$')
plt.plot(age,phot, color='green', label='$Q_{photo}$')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

#plt.text(1.02,6.46654,'$Q_{pair_{max}}=5.3x10^{13}erg/cm^3 s$')
#plt.text(1.76,13.4569,'$Q_{photo_{max}}=5.9x10^{11}erg/cm^3 s$')

#plt.legend(['plasma_neutrino,bremsstrahlung'])

# Energy loss -
#plt.xlabel('TEMP ($10^9 K$)')
# Temp9 - plt.xlabel('TEMP ($10^9 K$)')
# Luminosity -plt.xlabel('L)
#RAD (10^10 m)
plt.xlim(0,3.14191)
plt.ylim(-105,20)
plt.xlabel('Age(Myrs)',fontsize=13) 
plt.ylabel('$\log_{10}$Q(erg/cm\u00b3 s)',fontsize=13)
#(('$\u03C1$ ($10^6$ g /cm\u00b3)'))  # density
#plt.ylim(6.5845E-03,1.4092E+07) #energy
#plt.xlim(1.4189E+02,3.0026E+06) #temp.rho.rad
plt.legend(fontsize=13)
plt.show()
plt.savefig('p500q_age.jpg')
