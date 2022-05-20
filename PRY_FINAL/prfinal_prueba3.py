from ast import While
from calendar import c
from operator import index
import os
from tracemalloc import start
from clase_grabacion import AudioHelp
from github_grabar import aud
import threading
import time
from tkinter import END
from tkinter import *
from tkinter  import messagebox
from clase_starend_work import prin_fin_work
from pydub.playback import play
import serial
import pandas as pd
from scipy.io import wavfile
from pydub import AudioSegment
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import numpy
import math
from matplotlib.pylab import mpl

ventana=Tk()
variable_ini_grabacion = 0
variable_Serial = 0


ser = serial.Serial(
	port='COM5',\
	baudrate=9600,\
	parity=serial.PARITY_NONE,\
	stopbits=serial.STOPBITS_ONE,\
	bytesize=serial.EIGHTBITS,\
	timeout=0)

os.system('clear')


class MainAudio(threading.Thread):
    """ Clase para probar las funcionalidades del plugin AudioHelp. """
    
    

    def __init__(self):

        global variable_ini_grabacion
        self.work_reference =[]
        a = variable_ini_grabacion
        self.audio_help = AudioHelp()
        self.test_recording(a)
       
        

    def test_recording(self,a):

        """ 
            Función de ejecución secuencial para probar grabación, 
            reconocimiento de audio a texto y reproducción de audio. 
        """
        work_reference = []
        global variable_Serial
        vector_correlaciones = np.array([])
        vector_correlaciones2 = np.array([])
        vector_ref = ["patio","cocina","habitacion","sala"]
        # vector_ref = ["patio","cocina","habitacion","comedor"]
        vector_ref2 = ["luz","ventilador","puerta"]

        while 1:
            
            if variable_ini_grabacion == 1:
                

                sonido1= None
                self.ad = aud()
                self.Pincipio_fin = prin_fin_work()
                palabras = self.Pincipio_fin.reproducir()
                print("reproduciendo palabra 1")
                #play(palabras[0])
                time.sleep(0.3)
                print("reproduciendo palabra 2")
                #play(palabras[1])
                time.sleep(0.3)

                work_reference = []
                vector_correlaciones = np.array([])
                vector_correlaciones2 = np.array([])
                indice_maximo1 = indice_maximo2 = indice_maximo3 = indice_maximo4 = 0
                vector_ind = vector_ind2 = []

                rate,palabras_1 = wavfile.read('PRY_FINAL/recorte2.wav')
                amplitud = max(palabras_1)
                palabras_1 = palabras_1/amplitud
                tamaño1 = len(palabras_1)
                media_p1 = 0
                media_w=0

                for i in range(0,len(palabras_1)):
                    media_p1=palabras_1[i]+media_p1 

                prom_p1=media_p1/len(palabras_1)
                desviacion_p1= sum( (n-prom_p1)**2 for n in palabras_1)
                desviacion_p1= math.sqrt(desviacion_p1/len(palabras_1))
                 
                for n in range (0,4,1):
                    
                    for m in range (0,10,1):

                        rate,works = wavfile.read(f'./PRY_FINAL/palabras_referencia/work_{vector_ref[n]}{m + 1}.wav')
                        works = works/max(works)
                        tamaño2 = len(works)

                        for i in range(0,len(works)):
                            media_w=works[i]+media_w 

                        prom_w=media_w/len(works)
                        desviacion_w= sum( (n-prom_w)**2 for n in works)
                        desviacion_w= math.sqrt(desviacion_w/len(works))
                        
                        if tamaño1>tamaño2:
                            for k in range (0,tamaño1,1):
                                works = np.append(works,0)
                                tamaño2 = len(works)
                                if tamaño1 == tamaño2:
                                    break
                                else:
                                    pass

                        elif tamaño2>tamaño1:
                            for k in range(0,tamaño2,1):
                                palabras_1 = np.append(palabras_1,0)
                                tamaño1 = len(palabras_1)
                                if tamaño1 == tamaño2:
                                    break
                                else:
                                    pass
                        else:
                            break

                        XZ=0
                        for j in range(0,len(palabras_1)):
                            XZ=XZ+((palabras_1[j]-prom_p1)*(works[j]-prom_w))
                            XZ= XZ/(len(works))
                        
                        val_correlacion= XZ/(desviacion_p1*desviacion_w)         
                        vector_correlaciones = np.append(vector_correlaciones,val_correlacion)
                
                print(vector_correlaciones)

                rate,palabras_2 = wavfile.read('PRY_FINAL/recorte1.wav')
                amplitud = max(palabras_2)
                palabras_2 = palabras_2/amplitud
                tamaño3 = len(palabras_2)


                for n in range(0,3,1):

                    for m in range(0,10,1):

                        rate,works2 = wavfile.read(f'./PRY_FINAL/palabras_referencia/work_{vector_ref2[n]}{m + 1}.wav')
                        works2 = works2/max(works2)
                        tamaño4 = len(works2)

                        if tamaño3>tamaño4:
                            for k in range (0,tamaño3,1):
                                works2 = np.append(works2,0)
                                tamaño4 = len(works2)
                                if tamaño3 == tamaño4:
                                    break
                                else:
                                    pass
                        
                        elif tamaño4>tamaño3:

                            for k in range(0,tamaño4,1):
                                palabras_2 = np.append(palabras_2,0)
                                tamaño3 = len(palabras_2)
                                if tamaño3 == tamaño4:
                                    break
                                else:
                                    pass
                        else:
                            break


                        val_correlacion2 = cross_corr(palabras_2,works2)
                        vector_correlaciones2 = np.append(vector_correlaciones2,val_correlacion2)




                #indice_maximo = max(vector_correlaciones)
                #indice_maximo = np.where(vector_correlaciones==indice_maximo)[0][0]

                indice_maximo1 = sum(vector_correlaciones[0:10])
                indice_maximo2 = sum(vector_correlaciones[10:20])
                indice_maximo3 = sum(vector_correlaciones[20:30])
                indice_maximo4 = sum(vector_correlaciones[30:40])
                vector_ind = [indice_maximo1,indice_maximo2,indice_maximo3,indice_maximo4]
                idx = vector_ind.index(max(vector_ind))


                if idx == 0:
                    s = "patio"
                
                elif idx == 1:
                    s = "cocina"
                
                elif idx == 2:
                    s = "habitacion"

                elif idx == 3:

                    s = "sala"
    

                else:    
                    pass

                indice_maximo5 = sum(vector_correlaciones2[0:10])
                indice_maximo6 = sum(vector_correlaciones2[10:20])
                indice_maximo7 = sum(vector_correlaciones2[20:30])
                vector_ind2 = [indice_maximo5,indice_maximo6,indice_maximo7]
                idx2 = vector_ind2.index(max(vector_ind2))

                if idx2 == 0:
                    act = "luz"
                elif idx2 == 1:
                    act = "ventilador"
                
                elif idx2 == 2:
                    act = "puerta"


                else:    
                    pass

                cond_serial = f"{s} {act}"
                if cond_serial == "patio luz":
                    variable_Serial = 1
                
                elif cond_serial == "cocina puerta":
                    variable_Serial = 2 
                
                elif cond_serial == "cocina luz":
                    variable_Serial = 3
                
                elif cond_serial == "habitacion ventilador":
                    variable_Serial = 4  
                
                elif cond_serial == "habitacion luz":
                    variable_Serial = 5

                elif cond_serial == "sala luz":
                    variable_Serial = 6

                elif cond_serial == "sala puerta":
                    variable_Serial = 7

                elif cond_serial == "sala ventilador":
                    variable_Serial = 8
                
                else:
                    pass

                print(cond_serial)
                
                        
            
def cross_corr(set1, set2):


        return abs(np.sum(set1 * set2))           


def imprimir():
    global variable_ini_grabacion
    variable_ini_grabacion = 1
    print("hola\r\n")

segundos = 1
ventana.geometry("400x400+0+0")
ventana.title("aplicacion de grabacion")
Button(ventana, text="GRABAR",command = imprimir).place(x = 50 , y =200)

class com_serial(threading.Thread):

    def __init__(self):
            
        self.enviar()
    
    def enviar(self):

        while 1:

            global variable_Serial  
            if variable_Serial == 0:
                ser.write(b'\r\n')
            elif variable_Serial == 1:
                ser.write(b'a\r\n')
            elif variable_Serial == 2:
                ser.write(b'b\r\n')
            elif variable_Serial == 3:
                ser.write(b'c\r\n')
            elif variable_Serial == 4:
                ser.write(b'd\r\n')
            elif variable_Serial == 5:
                ser.write(b'e\r\n')
            elif variable_Serial == 7:
                ser.write(b'f\r\n')
            elif variable_Serial == 8:
                ser.write(b'g\r\n')
            elif variable_Serial == 9:
                ser.write(b'h\r\n')

            else:
                pass

            variable_Serial = 0          
            time.sleep(1)


if __name__ == '__main__':

  
    hilo2 = threading.Thread(target=MainAudio)
    hilo2.start()

    hilo3 = threading.Thread(target=com_serial)
    hilo3.start()  
ventana.mainloop()