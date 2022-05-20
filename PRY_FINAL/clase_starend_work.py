# -*- Coding: utf-8 -*-
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

from soupsieve import select
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
from tkinter.simpledialog import askfloat


class prin_fin_work():

    def __init__(self) -> None:

        p = pyaudio.PyAudio()

        RECORD_SECONDS = None
        palabra_vector = None
        data = []
        data2 = []
        arreglo = []
        cont_palabras = 0
        FORMAT = pyaudio.paInt16
        data_and_segundos = self.abrir_audio(data,RECORD_SECONDS)
        palabra_vector = self.procesar(data_and_segundos[0],
                      cont_palabras,data_and_segundos[1])
        
        #song_1 = self.reproducir(palabra_vector,data_and_segundos[0])


    def abrir_audio(self,data,RECORD_SECONDS):
    
        global palabra_vector
 
        
        #wf = wave.open('test_audio.wav', 'rb')
        rate, data = wavfile.read('PRY_FINAL/test_audio.wav')
        data = data/max(data)
        RECORD_SECONDS = len(data)/rate
        palabra_vector = np.arange(0,(RECORD_SECONDS*10000)-10000,1)
        song = AudioSegment.from_wav(r"C:\Users\Daniel Ramírez\OneDrive\Escritorio\cod_matlab2021\DSP_python\PRY_FINAL\test_audio.wav")
        play(song)
        print (rate)
        return [data,palabra_vector]


    def procesar(self,data,cont_palabras,palabra_vector):
        
        n = False
        w = False
        indice_minimo= 0
        indice_maximo= 0
        differ = 0
        cont_muestra = 0
        vector_energias=[]
        vec_pal = []
        tamaño = len(data)
        tamaño_pal_vector = len(palabra_vector)

        for i in range(0,tamaño,300):

            E = sum([n**2 for n in data[i:i+300]])
            vector_energias.append(E)
            if E <= 0.9:
                palabra_vector[i:i+300] = 0
            else:
                palabra_vector[i:i+300] = 1
            
        tamaño2 = len(palabra_vector)
        
        for k in range(0,tamaño2,1):
        
            if (k == tamaño2-1) and (palabra_vector[k] == 0):
                indice_maximo = cont_muestra + indice_minimo
            else:
                pass

            if palabra_vector[k] == 0:
                if n == False:
                    cont_muestra = 0
                    indice_minimo = k
                    n = not n
                else:
                    indice_minimo = indice_minimo
                    cont_muestra = cont_muestra + 1 
            else:
                indice_maximo = cont_muestra + indice_minimo
                n = False
            differ = indice_maximo -indice_minimo
            if differ <1500:
                palabra_vector[indice_minimo:indice_maximo+1] = 1
            else:
                pass

        for ind in range (1,tamaño,1):
            if palabra_vector[ind] == 0:
                w = False
            if (w == False) and (palabra_vector[ind] == 1):
                cont_palabras = cont_palabras + 1
                vec_pal.append(cont_palabras)
                w = True
        print(vec_pal)
        return palabra_vector
        

    def reproducir(self):
        
        palabra_vector
        num_palabra1 = 0
        num_palabra2 = 1
        inicios = []
        finales = []
        W = False

        for i in range (1,len(palabra_vector),1):
            if (W == False) and (palabra_vector[i] == 1 ):
                inicios.append(i)
                W = True
            elif (W == True) and (palabra_vector[i] == 0):
                finales.append(i)
                W = False
            else:
                pass
    
    
        t1 = inicios[num_palabra1-1]/8000
        t2 = finales[num_palabra1-1]/8000
                
        t3 = inicios[num_palabra2-1]/8000
        t4 = finales[num_palabra2-1]/8000

        song = AudioSegment.from_wav(r"C:\Users\Daniel Ramírez\OneDrive\Escritorio\cod_matlab2021\DSP_python\PRY_FINAL\test_audio.wav")
        
        palabra_1 = song[t1*1000:t2*1000]
        palabra_2 = song[t3*1000:t4*1000]

        palabra_1.export("PRY_FINAL/recorte1.wav",format = "wav")
        palabra_2.export("PRY_FINAL/recorte2.wav",format = "wav")
        return [palabra_2,palabra_1]
    

        



#g = prin_fin_work()
#g.__init__