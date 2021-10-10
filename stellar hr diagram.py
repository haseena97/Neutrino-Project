import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

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
lr1 = data1.lr
teff1 = data1.teff
lr2 = data2.lr
teff2 = data2.teff
lr3 = data3.lr
teff3 = data3.teff
lr4 = data4.lr
teff4 = data4.teff
lr5 = data5.lr
teff5 = data5.teff
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
#plt.title('Stellar H-R diagram',fontsize=15)
plt.plot(teff1,lr1,label='120M$_\odot$')
plt.plot(teff2,lr2,label='150M$_\odot$')
plt.plot(teff3,lr3,label='200M$_\odot$')
plt.plot(teff4,lr4,label='300M$_\odot$')
plt.plot(teff5,lr5,label='500M$_\odot$')

plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
#plt.text(4.82524,6.2653,'start',fontsize=13)
#plt.text(4.75381,7.10647,'end',fontsize=13)
#plt.plot(phot,lr)
legend = plt.legend(loc='upper left')
plt.xlim(4.9,3.87)
# Energy loss -
#plt.xlabel('TEMP ($10^9 K$)')
# Temp9 - plt.xlabel('TEMP ($10^9 K$)')
# Luminosity -plt.xlabel('L)
#RAD (10^10 m)

plt.xlabel('$\log_{10}$Teff(K)',fontsize=13) 
plt.ylabel('$\log_{10}$(L/$L_\odot$)',fontsize=13)
#(('$\u03C1$ ($10^6$ g /cm\u00b3)'))  # density
#plt.ylim(6.5845E-03,1.4092E+07) #energy
#plt.xlim(1.4189E+02,3.0026E+06) #temp.rho.rad
plt.show()
plt.savefig('stellarhr.jpg')
