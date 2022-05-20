# -- coding: utf-8 --
import chunk
from sre_parse import FLAGS
from tkinter import ttk
import math
from tkinter import ttk
import numpy as np   
#-------------------------------------------------------------------------------------------
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk #NavigationToolbar2TkAgg
#------------------------------------------------------------------------------------------
import tkinter as tk
#------------------------------------------------------------------------------------------
import wave
import struct
import scipy.io.wavfile as wavfile
import pyaudio
from doctest import master
from tkinter import *
from tkinter  import messagebox
from tkinter.simpledialog import askfloat

# -- coding: utf-8 --
from soupsieve import select
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
from tkinter.simpledialog import askfloat
import numpy as np
import statistics
import scipy.io.wavfile as wavfile
from math import sqrt



X = []
rate, X = wavfile.read('PRY_FINAL/recorte1.wav')
X = X/max(X)
rate, Z = wavfile.read('PRY_FINAL/palabras_referencia/work_luz1.wav')
Z=Z/max(Z)

tamaño1 = len(X)
tamaño2 = len(Z)

print(type(X))
#X = np.array(X)
#Z= np.array(Z)

mediax = 0
mediaz=0

l = abs(tamaño1-tamaño2)
c = np.zeros(l)
if tamaño2 > tamaño1: 
    X = np.append(X,c)
else:
    Z = np.append(Z,c)

tamaño1 = len(X)
tamaño2 = len(Z)


for i in range(0,len(X)):
    mediax=X[i]+mediax 

promx=mediax/len(X)

for i in range(0,len(Z)):
    mediaz=Z[i]+mediaz

promz=mediaz/len(Z)

plt.plot(X)
plt.plot(Z)
plt.show()
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

