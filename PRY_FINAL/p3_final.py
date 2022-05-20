# -- coding: utf-8 --
"""
Created on Wed Mar 16 11:41:43 2022

@author: Camilo
"""

import numpy as np
import statistics
import scipy.io.wavfile as wavfile
from math import sqrt
X=[1,2,3,4]
Z=[1,2,3,4]

rate, X = wavfile.read("PRY_FINAL/palabras_referencia/work_patio1.wav")
X = X/max(X)
rate, Z = wavfile.read("PRY_FINAL/palabras_referencia/work_patio2.wav")
Z=Z/max(Z)
mediax = 0
mediaz=0
for i in range(0,len(X)):
    mediax=X[i]+mediax 

promx=mediax/len(X)

for i in range(0,len(Z)):
    mediaz=Z[i]+mediaz

promz=mediaz/len(Z)


#desviacion estandar con libreria
desvx= statistics.pstdev(X)
#print(desvx)

desvz= statistics.pstdev(Z)
#print(desvz)

#desviacion estandar manual
desviacionx= sum( (n-promx)**2 for n in X)
desviacionx= sqrt(desviacionx/len(X))
#print('manualx ' +str(desviacionx))

desviacionz= sum( (n-promz)**2 for n in Z)
desviacionz= sqrt(desviacionz/len(Z))
#print('manualz '+ str(desviacionz))

XZ=0
for i in range(0,len(X)):
    XZ=XZ+((X[i]-promx)*(Z[i]-promz))
XZ= XZ/(len(Z))
print (XZ)


pearson= np.corrcoef(X,Z)[0][1]
print('coeficiente ' + str(pearson))
pearson= XZ/(desviacionx*desviacionz)
print('pearson con covarianza '+ str(pearson))