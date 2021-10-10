# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:59:38 2019

@author: haseena
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
#Input data that you want to analyse
data1 = pd.read_excel('Processed data g-file.xlsx' , sheet_name='P120')
data2 = pd.read_excel('Processed data g-file.xlsx' , sheet_name='P150')
data3 = pd.read_excel('Processed data g-file.xlsx' , sheet_name='P200')
data4 = pd.read_excel('Processed data g-file.xlsx' , sheet_name='P300')
data5 = pd.read_excel('Processed data g-file.xlsx' , sheet_name='P500')

params = {'figure.figsize':(6,5)}

plt.rcParams.update(params)
#Solar Luminosity
l0 = 3.838E26
#declare your column
#temp = data.temp
#rho = data.den
#rad = data.rad/1E10
mass1 = data1.mass
age1 = data1.agef
mass2 = data2.mass
age2 = data2.agef
mass3 = data3.mass
age3 = data3.agef
mass4 = data4.mass
age4 = data4.agef
mass5 = data5.mass
age5 = data5.agef
#pair = data.paired
#phot = data.photod
#plas = data.plas
#brem = np.log10(data.brem)
#recomb = data.recomb
#lxx = data.lxx/1E8
#total = data.total
#eps120 = data.epsnu

#print(eps120,rad)

#plotting configuration
#plt.style.use('seaborn')
#plt.title('Kippenhahn diagram',fontsize=15)
plt.plot(age1,mass1,label='120$M_\odot$')
plt.plot(age2,mass2,label='150$M_\odot$')
plt.plot(age3,mass3,label='200$M_\odot$')
plt.plot(age4,mass4,label='300$M_\odot$')
plt.plot(age5,mass5,label='500$M_\odot$')
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
#plt.plot(phot,lr)
#plt.legend(['plasma_neutrino,bremsstrahlung'])

# Energy loss -
#plt.xlabel('TEMP ($10^9 K$)')
# Temp9 - plt.xlabel('TEMP ($10^9 K$)')
# Luminosity -plt.xlabel('L)
#RAD (10^10 m)
legend = plt.legend()
plt.xlim(0,3.10)
plt.xlabel('Age(Myrs)',fontsize=13) 
plt.ylabel('M($M_\odot$)',fontsize=13)
#(('$\u03C1$ ($10^6$ g /cm\u00b3)'))  # density
#plt.ylim(6.5845E-03,1.4092E+07) #energy
#plt.xlim(1.4189E+02,3.0026E+06) #temp.rho.rad
plt.show()
plt.savefig('kippenhahn.jpg')
