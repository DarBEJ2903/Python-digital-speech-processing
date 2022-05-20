import chunk
from pydoc import text
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

#Declaraciòn de variables globales



def grabar():
    
    global data
    global cont_palabras
    global chunk,FORMAT,CHANNELS,RATE,RECORD_SECONDS,samples
    global arreglo
    global palabra_vector

    data = []
    arreglo = []

    ax.clear()
    cont_palabras = 0
    
    entry.config(state=tk.NORMAL)
    entry.delete(0,"end")
    
    label1 = ttk.Label(ventana, text=f"grabando")
    label1.place(x=500, y=400) 



    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=CHANNELS,rate =RATE,input=True,frames_per_buffer=chunk)

    print ("grabando")

    
    for i in range(0, int(samples)):
            data = stream.read(chunk)
            arreglo.append(data)
            

    stream.stop_stream()
    stream.close()
 

    wf = wave.open('dato.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setframerate(RATE)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.writeframes(b''.join(arreglo))
    wf.close()
    print ("fin")

    rate, data = wavfile.read("dato.wav")
    data = data/max(data)
    kp = len(data)
    ks = len (palabra_vector)
    print (rate)
    
    
    ax.plot(data)
    canvas.draw()
    

    

def procesar():

    global data,cont_palabras,palabra_vector
    n = False
    w = False
    indice_minimo= 0
    indice_maximo= 0
    differ = 0
    cont_muestra = 0
    vector_energias=[]
    vec_pal = []
    tamaño = len(data)

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
    
    for i in range (1,tamaño,1):
        if palabra_vector[i] == 0:
            w = False
        if (w == False) and (palabra_vector[i] == 1):
            cont_palabras = cont_palabras + 1
            vec_pal.append(cont_palabras)
            w = True
    
    combo["values"] = vec_pal

    entry.insert(0,cont_palabras)
    messagebox.showinfo("Cantidad de palabras", ["Se detectaron:"," ",cont_palabras," palabras"])



def reproducir():
    

    global cont_palabras,data,palabra_vector
    global chunk,FORMAT,CHANNELS,RATE,RECORD_SECONDS,samples
    global arreglo
    global data2
    W = False
    palabra = 0
    inicios = []
    finales = []

    for i in range (1,len(palabra_vector),1):
        if (W == False) and (palabra_vector[i] == 1 ):
            inicios.append(i)
            W = True
        elif (W == True) and (palabra_vector[i] == 0):
            finales.append(i)
            W = False
        else:
            pass
    
    for n in range (0,cont_palabras,1):

        palabra = palabra + 1
        t1 = inicios[palabra-1]/8000
        t2 = finales[palabra-1]/8000
        song = AudioSegment.from_wav(r"C:\Users\Daniel Ramírez\OneDrive\Escritorio\cod_matlab2021\DSP_python\dato.wav")
        song_1 = song[t1*1000:t2*1000]
        song_1.export(f"PRY_FINAL/palabras_referencia/work_ventilador{n+1}.wav", format="wav")
        

    palabra = 0



    print(inicios)
    palabra = int(combo.get())
    t1 = inicios[palabra-1]/8000
    t2 = finales[palabra-1]/8000
    song = AudioSegment.from_wav(r"C:\Users\Daniel Ramírez\OneDrive\Escritorio\cod_matlab2021\DSP_python\dato.wav")
    song_1 = song[t1*1000:t2*1000]
    play(song_1)
    song_1.export("dato5.wav",format = "wav")
    print(palabra)
    ax.clear()
    ax.plot(data[inicios[palabra-1]:finales[palabra-1]])
    canvas.draw()

    




#creando la ventana 
ventana=Tk()
ventana.geometry("1080x900+0+0")
ventana.title("aplicacion de grabacion")

# plt.ion()

fig,ax = plt.subplots(figsize=(10,4),dpi=100)
canvas=FigureCanvasTkAgg(fig,master = ventana)
canvas.get_tk_widget().pack()

#Creacion de una caja de text0
entry = ttk.Entry()
entry.place(x=800, y=400)

#creacion de un combobox o caja de opciones
combo = ttk.Combobox()
combo.place(x = 300, y = 400)

entry2 = ttk.Entry()
entry2.place(x=300, y=400)

#Creacion de un Label

label = Label(ventana,text="Numero de palabras")
label.place(x = 680 , y = 400)

RECORD_SECONDS = askfloat("Parametros de Grabaciòn", "Tiempo de grabaciòn")
RATE = 8000
samples = (RATE/3024)*RECORD_SECONDS
palabra_vector = np.arange(0,(RECORD_SECONDS*10000)-10000,1)

data = []
data2 = []
arreglo = []
cont_palabras = 0
chunk = 3024
FORMAT = pyaudio.paInt16
CHANNELS = 1



#Creaciòn de botones
Button(ventana, text="GRABAR", command=grabar).place(x = 50 , y =400)
Button(ventana, text="PROCESAR", command=procesar).place(x = 110, y = 400)
Button(ventana, text="REPRODUCIR", command=reproducir).place(x = 200, y = 400)









ventana.mainloop()


















 




